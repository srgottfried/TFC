from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUttered
import sys

sys.path.append("utils")
from rocketchat_api_calls import get_user_info


class ActionPizzaSubmit(Action):
    """
    It is thrown at the end of a form to process the required slots.
    Sets the form slots to None, allowing the form to be relaunched again.
    """

    def name(self) -> Text:
        return "action_pizza_submit"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        username = tracker.slots.get("user_name")
        pizza_slots = {
            "pizza_type": tracker.slots.get("pizza_type"),
            "pizza_size": tracker.slots.get("pizza_size"),
        }

        message = f"Procesando pedido de {username}: "
        for slot_name, slot_value in pizza_slots.items():
            if slot_value is not None:
                message += f"\n{slot_name}: {slot_value}"

        dispatcher.utter_message(text=message)

        return [SlotSet("pizza_type", None), SlotSet("pizza_size", None)]
