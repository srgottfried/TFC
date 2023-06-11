from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionCheckForm(Action):
    """
    Checks if there is a form in progress at the time another form is launched.
    If so, it kills the current form and launches the new for, avoiding launching one form within another.
    """

    def name(self) -> Text:
        return "action_check_form"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        active_loop = tracker.active_loop.get("name")

        if active_loop:
            return [SlotSet("requested_slot", None), SlotSet("intent", None)]

        return []
