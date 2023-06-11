import requests
import json
from typing import Any, Text

URL_USERS_INFO = "http://rocketchat:3000/api/v1/users.info"
URL_USERS_SET_STATUS = url = "http://rocketchat:3000/api/v1/users.setStatus"

HEADERS = {
    "X-Auth-Token": "CORQcdw9WpWV9d-RJOWaxJ-laNlBPzrnrkRh67qowfP",
    "X-User-Id": "vccXJAJYf2ZXSscCm",
    "Content-type": "application/json",
}

BOT_HEADERS = {
    "X-Auth-Token": "ns-WHhRW7zWQbDgMdrz6_qFjPu3ZHvQtdsjR-jxj9Cf",
    "X-User-Id": "Pt9d7aKFzbXWj8kvt",
    "Content-type": "application/json",
}

HHEADERS = {
    "X-Auth-Token": "ovpGYU34PXxANqe28rt4jRJ8h_K21PSpNYqep1ovUdM",
    "X-User-Id": "82QyYu6NweoHRYSWX",
    "Content-type": "application/json",
}


def get_user_info(user_id: Text) -> Any:
    params = {"userId": f"{user_id}"}

    response = requests.get(URL_USERS_INFO, headers=HEADERS, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise requests.RequestException("USER INFO could not be accessed.")


def set_user_status_online() -> Any:
    data = {"status": "online"}

    response = requests.post(
        URL_USERS_SET_STATUS, headers=HEADERS, data=json.dumps(data)
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise requests.RequestException("USER STATUS could not be modify.")


if __name__ == "__main__":
    URL_USERS_INFO = "http://localhost:3000/api/v1/users.info"
    URL_USERS_SET_STATUS = url = "http://localhost:3000/api/v1/users.setStatus"
    set_user_status_online()