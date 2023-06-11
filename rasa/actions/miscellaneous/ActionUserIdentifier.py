from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json
import sys

sys.path.append("utils")
from rocketchat_api_calls import get_user_info


class ActionUserIdentifier(Action):
    """
    Check and store in a slot the user of the conversation.
    """

    def name(self) -> Text:
        return "action_user_identifier"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        if not tracker.slots.get("user"):
            self.tracker = tracker
            user_id = self._digest_sender_id()

            if user_id:
                user_data = get_user_info(user_id).get("user")
                user_name = user_data.get("name")
            else:
                user_data = None
                user_name = "usuario"

            return [SlotSet("user", user_data), SlotSet("user_name", user_name)]

        return []

    def _digest_sender_id(self) -> Optional[Text]:
        try:
            sender_id = self.tracker.sender_id
            if len(sender_id) != 34:
                return None
            sender_id_1 = sender_id[:17]
            sender_id_2 = sender_id[17:]
            
            try:
                rol = get_user_info(sender_id_1).get("user").get("roles")
                if rol == None:
                    rol = []
            except Exception as e:
                rol = ["other"]

            if "bot" in rol:
                user_id = sender_id_2
            else:
                user_id = sender_id_1
            return user_id
        except Exception as e:
            print(e)
            return None
