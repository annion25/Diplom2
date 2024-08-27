import allure
from user_creation_api import UserCreation
from user_delete_api import UserDelete
from order_creation_api import OrderCreation
from order_user_api import GetUserOrders


class TestGetUserOrders:

    @allure.title("Проверка получения списка заказов авторизованным пользователем")
    @allure.description("Получение списка заказов авторизованным пользователем, проверка кода ответа и тела ответа")
    def test_get_order_list_with_one_order_with_auth_success(self):
        user_creation_data = UserCreation.register_new_user_and_return_email_password(
            self, 10, 10, 10)
        user_creation_email_pass = user_creation_data[0]
        ingredients = OrderCreation.order_some_ingredients_get(self)
        OrderCreation.order_creation(self, ingredients, user_creation_email_pass[3])
        order_list_response = GetUserOrders.get_users_orders(self, user_creation_email_pass[3])

        assert order_list_response.status_code == 200 and order_list_response.json()["success"] == True

        user_email_data = user_creation_email_pass[0]
        user_pass_data = user_creation_email_pass[1]
        user_token_data = user_creation_email_pass[3]
        UserDelete.user_delete(self, user_email_data, user_pass_data, user_token_data)

    @allure.title("Проверка получения списка заказов неавторизованным пользователем")
    @allure.description("Получение списка заказов неавторизованным пользователем, проверка кода ответа и тела ответа")
    def test_get_order_list_no_auth_fail(self):
        order_list_response = GetUserOrders.get_users_orders(self, "")

        assert order_list_response.status_code == 401 and order_list_response.json()["success"] == False

