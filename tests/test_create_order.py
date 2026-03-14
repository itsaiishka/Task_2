import allure
from helpers.order_helpers import get_ingredients, create_order

class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, create_test_user):
        access_token = create_test_user["accessToken"]

        ingredients_response = get_ingredients().json()["data"]
        ingredients = [
            ingredients_response[0]["_id"],
            ingredients_response[1]["_id"]
        ]

        response = create_order(ingredients, access_token)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["success"] is True
        assert "order" in response_json

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        ingredients_response = get_ingredients().json()["data"]
        ingredients = [
            ingredients_response[0]["_id"],
            ingredients_response[1]["_id"]
        ]

        response = create_order(ingredients)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, create_test_user):
        access_token = create_test_user["accessToken"]

        response = create_order([], access_token)
        response_json = response.json()

        assert response.status_code == 400
        assert response_json["success"] is False
        assert response_json["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredients(self, create_test_user):
        access_token = create_test_user["accessToken"]

        invalid_ingredients = ["invalid_id1"]

        response = create_order(invalid_ingredients, access_token)

        assert response.status_code == 500
        