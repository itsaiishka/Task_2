import allure
from helpers.order_helpers import get_ingredients, create_order, get_user_orders


class TestGetUserOrders:
    @allure.title("Получение заказов пользователя с авторизацией")
    def test_get_user_orders_with_auth(self, create_test_user):
        access_token = create_test_user["accessToken"]

        ingredients_response = get_ingredients().json()["data"]
        ingredients = [
            ingredients_response[0]["_id"],
            ingredients_response[1]["_id"]
        ]

        create_order(ingredients, access_token)

        response = get_user_orders(access_token)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["success"] is True
        assert "orders" in response_json

    @allure.title("Получение заказов пользователя без авторизации")
    def test_get_user_orders_without_auth(self, access_token=None):
        response = get_user_orders(access_token)
        response_json = response.json()

        assert response.status_code == 401
        assert response_json["success"] is False
        assert response_json["message"] == "You should be authorised"