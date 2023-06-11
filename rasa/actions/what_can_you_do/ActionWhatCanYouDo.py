import sys

sys.path.append("utils")
from messages import Message
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionWhatCanYouDo(Action):
    """
    Explains bot skills.
    """

    def name(self) -> Text:
        return "action_what_can_you_do"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        payload = "Puedo ayudarte con diferentes tareas:"
        attachmets = [
            {
                "color": "#ff0000",
                "button_alignment": "horizontal",
                "actions": [
                    {
                        "type": "button",
                        "text": "Pedir una pizza",
                        "msg": "Quiero pedir una pizza",
                        "msg_in_chat_window": True,
                    },
                    {
                        "type": "button",
                        "text": "Información sobre Gradiant",
                        "msg": "¿Dónde está Gradiant?",
                        "msg_in_chat_window": True,
                    },
                    {
                        "type": "button",
                        "text": "Vigilancia tecnológica",
                        "msg": "https://www.newscientist.com/subject/space",
                        "msg_in_chat_window": True,
                    },
                ],
            }
        ]
        message = Message(payload, attachmets)

        dispatcher.utter_message(json_message=message)
        return []
