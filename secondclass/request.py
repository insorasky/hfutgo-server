import requests
import json


def sc_request(method, userid, url, params=None, json_data=None):
    headers = {'key_session': userid}
    if params is None:
        params = []
    if json_data is not None:
        headers.update({'Content-Type': 'application/json'})
    data = requests.request(method, url, params=params, headers=headers, json=json_data).json()
    return data
