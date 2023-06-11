from typing import Any, Text, Dict, Union, List
from rasa_sdk import Tracker
import requests

API_ENDPOINT_FOR_POST_SURVEILLANCE_OPERATIONS = "http://fastapi:8000/"


class Payload(Dict):
    """Build a payload from the tracker applying the appropriate slot filter."""

    def __init__(
        self, tracker: Tracker, filter: Union[Dict[Text, Text], None] = None
    ) -> None:
        self._filter = filter
        self._tracker = tracker
        self._build_payload_from_tracker_using_filters()

    def _build_payload_from_tracker_using_filters(self) -> None:
        try:
            payload = {}
            if self._filter and self._tracker:
                for k, v in self._filter.items():
                    payload[k] = self._tracker.slots.get(v)
            else:
                for k, v in self._tracker.slots.items():
                    payload[k] = v
            self.update(payload)
        except Exception as e:
            raise Exception("Error building payload: " + e)

    @property
    def filter(self) -> Dict[Text, Text]:
        return self._filter

    @filter.setter
    def filter(self, filter: Dict[Text, Text]) -> None:
        self._filter = filter
        self._build_payload_from_tracker_using_filters()


class Message(Dict):
    """Build a message based on a payload and the attachments."""

    def __init__(
        self,
        payload: Union[Payload, Text],
        attachments: Union[List[Dict[Text, Text]], None] = None,
    ) -> None:
        self._payload = payload
        self._attachments = attachments
        self._build_message_from_payload_with_attachments()

    def _build_message_from_payload_with_attachments(self):
        if self._attachments:
            message = {
                "text": str(self._payload),
                "attachments": self._attachments,
            }
        else:
            message = {"text": str(self._payload)}
        self.update(message)

    @property
    def attachments(self) -> List[Dict[Text, Text]]:
        return self._attachments

    @attachments.setter
    def attachments(self, attachments: List[Dict[Text, Text]]) -> None:
        self._attachments = attachments
        self._build_message_from_payload_with_attachments()


class OutputTemplateMessage(Message):
    def __init__(
        self,
        payload: Union[Payload, Text],
        attachments: Union[List[Dict[Text, Text]], None] = None,
        format: List[Text] = None,
    ) -> None:
        self._format = format
        super().__init__(payload, attachments)

    def _build_message_from_payload_with_attachments(self):
        format_message = ""
        if type(self._payload) == Payload:
            for elem in self._format:
                format_message += (
                    f">*{str(elem).upper()}*: " + str(self._payload.get(elem)) + "\n"
                )
        elif type(self._payload) == Text:
            format_message += self._payload

        if self._attachments:
            message = {
                "text": str(format_message),
                "attachments": self._attachments,
            }
        else:
            message = {"text": str(format_message)}
        self.update(message)


class ApiConnector:
    def post_payload(self, payload: Payload) -> Text:
        response = requests.post(
            API_ENDPOINT_FOR_POST_SURVEILLANCE_OPERATIONS, json=payload
        )
        return response
