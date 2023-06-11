from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

VALID_AREA = ["SI", "CA", "COM", "SEC", "EHEALTH", "MM"]
VALID_TYPE = ["VIGILANCIA TECNOLÓGICA", "VIGILANCIA DEL ENTORNO"]
VALID_SECTOR = ["TELECOMMUNICATION", "AIR AND SPACE", "HEALTH AND WELLBEING", "INDUSTRY", "OTHER"]

class ValidateSurveillanceForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_surveillance_form"

    def validate_title(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        dispatcher.utter_message(text=f":white_check_mark: Título actualizado")
        return {"title": slot_value}

    def validate_description(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        dispatcher.utter_message(text=f":white_check_mark: Descripción actualizada")
        return {"description": slot_value}

    def validate_area(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        area = tracker.slots.get("area")
        if area in VALID_AREA:
            dispatcher.utter_message(text=f":white_check_mark: Área actualizada")
            return {"area": slot_value}
        else:
            dispatcher.utter_message(text=f":red_circle: El área introducida no es válida")
            return {"area": None}

    def validate_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        type = tracker.slots.get("type")
        if type in VALID_TYPE:
            dispatcher.utter_message(text=f":white_check_mark: Tipo actualizado")
            return {"type": slot_value}
        else:
            dispatcher.utter_message(text=f":red_circle: El tipo introducido no es válido")
            return {"type": None}

    def validate_sector(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        sector = tracker.slots.get("sector")
        if sector in VALID_SECTOR:
            dispatcher.utter_message(text=f":white_check_mark: Sector actualizado")
            return {"sector": slot_value}
        else:
            dispatcher.utter_message(text=f":red_circle: El sector introducido no es válido")
            return {"sector": None}

    def validate_url(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        return {"url": slot_value}
    
