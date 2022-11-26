import requests


def post_cake(payload):
    url = 'http://127.0.0.1:8000/cake/'
    response = requests.post(url, params=payload)
    response.raise_for_status()

    return response.json()