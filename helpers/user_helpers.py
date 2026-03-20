import requests
from helpers.endpoints import BASE_URL, CREATE_USER, LOGIN_USER, USER_DATA

def create_user(email, password, name):
    url = BASE_URL + CREATE_USER
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(url, json=payload)
    return response

def login_user(email, password):
    url = BASE_URL + LOGIN_USER
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(url, json=payload)
    return response

def delete_user(access_token):
    url = BASE_URL + USER_DATA
    headers = {
        "Authorization": access_token
    }
    response = requests.delete(url, headers=headers)
    return response