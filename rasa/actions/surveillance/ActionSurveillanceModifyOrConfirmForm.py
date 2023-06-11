from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUttered
import sys

sys.path.append("utils")
from rocketchat_api_calls import get_user_info
from messages import Payload, Message, OutputTemplateMessage


class ActionSurveillanceModifyOrConfirmForm(Action):
    def name(self) -> Text:
        return "action_surveillance_modify_or_confirm_form"

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

        attachments = [
            {
                "text": "¿Quieres modificar algún campo antes de guardar?",
                "button_alignment": "horizontal",
                "actions": [
                    {
                        "type": "button",
                        "text": "No",
                        "msg": "No quiero modificar ningún campo",
                        "msg_in_chat_window": True,
                    },
                    {
                        "type": "button",
                        "text": "Título",
                        "msg": "Quiero modificar el campo title",
                        "msg_in_chat_window": True,
                    },
                    {
                        "type": "button",
                        "text": "Descripción",
                        "msg": "Quiero modificar el campo description",
                        "msg_in_chat_window": True,
                    },
                    {
                        "type": "button",
                        "text": "Área",
                        "msg": "Quiero modificar el campo area",
                        "msg_in_chat_window": True,
                    },
                    {
                        "type": "button",
                        "text": "Tipo",
                        "msg": "Quiero modificar el campo type",
                        "msg_in_chat_window": True,
                    },
                    {
                        "type": "button",
                        "text": "Sector",
                        "msg": "Quiero modificar el campo sector",
                        "msg_in_chat_window": True,
                    },
                ],
            }
        ]

        message = OutputTemplateMessage(
            payload=payload,
            attachments=attachments,
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

        dispatcher.utter_message(json_message=message)

        return []
