import requests
import allure
import random
import pytest
from helpers.endpoints import BASE_URL, USER_DATA


class TestUpdateUser:

    @allure.title("Изменение любого поля пользователя с авторизацией")
    @pytest.mark.parametrize("field,value", [
        ("name", "Updated Name"),
        ("email", None),
        ("password", "updated_password")
    ])
    def test_update_user_with_auth(self, create_test_user, field, value):
        if field == "email":
            value = f"updated_email{random.randint(1000, 9999)}@example.com"

        access_token = create_test_user["accessToken"]

        update_payload = {field: value}

        headers = {"Authorization": access_token}

        response = requests.patch(BASE_URL + USER_DATA, json=update_payload, headers=headers)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json.get("success") is True


    @allure.title("Изменение любого поля пользователя без авторизации")
    @pytest.mark.parametrize("field,value", [
        ("name", "Updated Name"),
        ("email", "updated_email@example.com"),
        ("password", "updated_password")
    ])
    def test_update_user_without_auth(self, field, value):

        update_payload = {field: value}

        response = requests.patch(BASE_URL + USER_DATA, json=update_payload)
        response_json = response.json()

        assert response.status_code == 401
        assert response_json.get("success") is False