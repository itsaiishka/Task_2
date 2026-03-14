import requests
import allure
import uuid
from helpers.endpoints import BASE_URL, CREATE_USER


class TestCreateUser:
    @allure.title("Создание нового уникального пользователя")
    def test_create_unique_user(self):
        email = f"unique{uuid.uuid4()}@example.com"
        password = "unique_password"
        name = "Unique User"

        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        
        response = requests.post(BASE_URL + CREATE_USER, json=payload)

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, create_test_user):
        email = create_test_user["email"]
        password = create_test_user["password"]
        name = create_test_user["name"]

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(BASE_URL + CREATE_USER, json=payload)

        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == "User already exists"

    @allure.title("Создать пользователя и не заполнить одно из обязательных полей")
    def test_create_user_missing_fields(self):
        email = f"missing{uuid.uuid4()}@example.com"
        password = "missing_password"

        payload = {
            "email": email,
            "password": password
        }

        response = requests.post(BASE_URL + CREATE_USER, json=payload)

        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == "Email, password and name are required fields" 