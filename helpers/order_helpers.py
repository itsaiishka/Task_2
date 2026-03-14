import requests
from helpers.endpoints import BASE_URL, GET_INGREDIENTS, CREATE_ORDER

def get_ingredients():
    url = BASE_URL + GET_INGREDIENTS
    response = requests.get(url)
    return response

def create_order(ingredients, access_token=None):
    url = BASE_URL + CREATE_ORDER
    payload = {
        "ingredients": ingredients
    }
    headers = {}

    if access_token:
        headers["Authorization"] = access_token
    response = requests.post(url, json=payload, headers=headers)
    return response