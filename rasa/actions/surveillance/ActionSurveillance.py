import sys

sys.path.append("utils/scraper")
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from WebScraper import WebScraper
from messages import Message


class ActionSurveillance(Action):
    """
    Process urls for technological surveillance.
    """

    def name(self) -> Text:
        return "action_surveillance"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        try:
            self.tracker = tracker
            self.domain = domain

            url = tracker.slots.get("url")
            metadata = self._get_metadata_from(url)

            payload = self._get_text_payload_from_metadata_using_order_filter(
                metadata,
                order_filter=[
                    "title",
                    "user",
                    "date",
                    "area",
                    "type",
                    "sector",
                    "url",
                    "description",
                ],
            )
            attachments = [
                {
                    "button_alignment": "horizontal",
                    "actions": [
                        {
                            "type": "button",
                            "text": "Completar datos",
                            "msg": "Completar vigilancia tecnológica",
                            "msg_in_chat_window": True,
                        },
                    ],
                }
            ]
            message = Message(
                payload=payload,
                attachments=attachments,
            )
            dispatcher.utter_message(json_message=message)

            return [
                SlotSet("url", url),
                SlotSet("date", metadata["date"]),
                SlotSet("description", metadata["description"]),
                SlotSet("title", metadata["title"]),
                SlotSet("area", metadata["area"]),
                SlotSet("type", metadata["type"]),
                SlotSet("sector", metadata["sector"]),
            ]
        except Exception as e:
            utter_url_fail = (
                self._get_utter_response_from_domain("utter_url_fail") + ": " + str(e)
            )

            dispatcher.utter_message(text=utter_url_fail)
            return [SlotSet("url", None)]

    def _get_utter_response_from_domain(self, utter_name: Text) -> Text:
        return self.domain.get("responses").get(utter_name)[0].get("text")

    def _get_metadata_from(self, url: Text) -> Dict[Text, Any]:
        metadata = WebScraper(url).get_all_data
        self._add_user_name_to(metadata)
        return metadata

    def _add_user_name_to(self, metadata: Dict[Text, Any]) -> None:
        try:
            metadata["user"] = self.tracker.slots.get("user").get("username")
        except:
            metadata["user"] = "channel"

    def _get_text_payload_from_metadata_using_order_filter(
        self, metadata: Dict[Text, Any], order_filter: List[Text]
    ) -> Text:
        payload = ""
        for elem in order_filter:
            payload += f">*{str(elem).upper()}*: {metadata.get(elem)}\n"
        print(payload)
        payload = payload.replace("None", "")
        return payload
