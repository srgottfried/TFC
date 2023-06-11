from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, ActiveLoop


class ActionSurveillanceModify(Action):
    def name(self) -> Text:
        return "action_surveillance_modify"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        if tracker.slots["title"] and tracker.slots["url"]:
            modificable_slot = tracker.slots["modificable_slot"]
            return [
                SlotSet(str(modificable_slot), None),
                SlotSet("modificable_slot", None),
                ActiveLoop("surveillance_form"),
            ]
        else:
            return [SlotSet("modificable_slot", None)]
