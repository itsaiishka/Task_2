import requests
import allure
import random
from helpers.endpoints import BASE_URL, LOGIN_USER


class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, create_test_user):
        email = create_test_user["email"]
        password = create_test_user["password"]

        payload = {
            "email": email,
            "password": password
        }

        response = requests.post(BASE_URL + LOGIN_USER, json=payload)
        response_json = response.json()

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "accessToken" in response_json

    @allure.title("Логин с неверным логином и паролем")
    def test_login_invalid_user(self):
        email = f"invalid{random.randint(1000, 9999)}@example.com"
        password = "invalid_password"

        payload = {
            "email": email,
            "password": password
        }

        response = requests.post(BASE_URL + LOGIN_USER, json=payload)
        response_json = response.json()

        assert response.status_code == 401
        assert response_json.get("success") is False
        assert response_json.get("message") == "email or password are incorrect"