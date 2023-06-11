from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUttered
import sys

sys.path.append("utils")
from rocketchat_api_calls import get_user_info
from messages import Payload, OutputTemplateMessage, ApiConnector


class ActionSurveillanceSubmitForm(Action):
    def name(self) -> Text:
        return "action_surveillance_submit_form"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        filter = {
            "user": "user_name",
            "date": "date",
            "url": "url",
            "description": "description",
            "title": "title",
            "area": "area",
            "type": "type",
            "sector": "sector",
        }
        payload = Payload(tracker=tracker, filter=filter)
        message = OutputTemplateMessage(
            payload=payload,
            format=[
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

        if tracker.slots["title"] and tracker.slots["url"]:
            dispatcher.utter_message(json_message=message)
            print(ApiConnector().post_payload(payload))

        return [
            SlotSet("url", None),
            SlotSet("description", None),
            SlotSet("title", None),
            SlotSet("area", None),
            SlotSet("type", None),
            SlotSet("sector", None),
        ]
