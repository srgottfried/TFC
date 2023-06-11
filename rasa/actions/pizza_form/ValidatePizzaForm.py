from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

type_db = [
    "fungi",
    "napolitana",
    "carbonara",
    "cuatro quesos",
    "cuatro estaciones",
]
size_db = [
    "pequeña",
    "mediana",
    "grande",
    "familiar",
]


class ValidatePizzaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_pizza_form"

    def validate_pizza_type(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        
        request_type = next(tracker.get_latest_entity_values("pizza_type"), None)
        
        if request_type.lower() not in type_db:
            dispatcher.utter_message(text="No tenemos esa pizza en carta.")
            return {"pizza_type": None}
        dispatcher.utter_message(text=f"La {request_type} es una buena elección.")
        return {"pizza_type": slot_value}


    def validate_pizza_size(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        
        request_size = next(tracker.get_latest_entity_values("pizza_size"), None)
        
        if request_size.lower() not in size_db:
            dispatcher.utter_message(text="No tenemos ese tamaño de pizza.")
            return {"pizza_size": None}
        dispatcher.utter_message(text=f"La {request_size} tiene el tamaño perfecto.")
        return {"pizza_size": slot_value}