import allure
import user_delete_api, user_creation_api, order_creation_and_get_ingredients_api


class TestOrderCreation:

    @allure.title("Проверка успешного создания заказа")
    @allure.description("Создание заказа с выбранными ингредиентами авторизованным пользователем, проверка статуса "
                        "ответа и тела ответа ")
    def test_order_creation_with_auth_with_ingredients_success(self):
        user_creation_data = user_creation_api.UserCreation.register_new_user_and_return_email_password(
            self, 10, 10, 10)
        user_creation_email_pass = user_creation_data[0]
        ingredients = order_creation_and_get_ingredients_api.OrderCreation.order_some_ingredients_get(self)
        response = order_creation_and_get_ingredients_api.OrderCreation.order_creation(self, ingredients,
                                                                                       user_creation_email_pass[3])

        assert (response.status_code == 200 and response.json()["success"] == True and
                response.json()["order"]["owner"]["name"] == user_creation_email_pass[2])

        user_email_data = user_creation_email_pass[0]
        user_pass_data = user_creation_email_pass[1]
        user_token_data = user_creation_email_pass[3]
        user_delete_api.UserDelete.user_delete(self, user_email_data, user_pass_data, user_token_data)

    @allure.title("Проверка создания заказа неавторизованным пользователем")
    @allure.description(
        "Создание заказа с выбранными ингредиентами неавторизованным пользователем, "
        "проверка статуса ответа и тела ответа ")
    def test_order_creation_without_auth_with_ingredients_fail(self):
        ingredients = order_creation_and_get_ingredients_api.OrderCreation.order_some_ingredients_get(self)
        response = order_creation_and_get_ingredients_api.OrderCreation.order_creation(self, ingredients, "")
        assert (response.status_code == 200 and response.json()["success"] == True and
                "status" not in response.json()["order"])
        #сомневаюсь на счет такого ассерта, не думаю, что без авторизации должен приходить код 200 и success= True, при
        #этом заказ не виден в списке заказов, больше похоже на баг в проде

    @allure.title("Проверка создания заказа авторизованным пользователем без ингредиентов")
    @allure.description(
        "Создание заказа без ингредиентов авторизованным пользователем, проверка статуса ответа и тела ответа ")
    def test_order_creation_with_auth_no_ingredients_fail(self):
        user_creation_data = user_creation_api.UserCreation.register_new_user_and_return_email_password(
            self, 10, 10, 10)
        user_creation_email_pass = user_creation_data[0]
        response = order_creation_and_get_ingredients_api.OrderCreation.order_creation(self, "",
                                                                                       user_creation_email_pass[3])

        assert response.status_code == 400 and response.json()["success"] == False

        user_email_data = user_creation_email_pass[0]
        user_pass_data = user_creation_email_pass[1]
        user_token_data = user_creation_email_pass[3]
        user_delete_api.UserDelete.user_delete(self, user_email_data, user_pass_data, user_token_data)

    @allure.title("Проверка создания заказа авторизованным пользователем с неверным хэшем ингредиентов")
    @allure.description("Создание заказа с неверным хэшем ингредиентов авторизованным пользователем, "
            "проверка статуса ответа и тела ответа ")
    def test_order_creation_with_auth_incorrect_ingredients_fail(self):
        user_creation_data = user_creation_api.UserCreation.register_new_user_and_return_email_password(
                self, 10, 10, 10)
        user_creation_email_pass = user_creation_data[0]
        ingredients = order_creation_and_get_ingredients_api.OrderCreation.order_some_ingredients_get(self)
        response = order_creation_and_get_ingredients_api.OrderCreation.order_creation(self, ingredients[0] + 'tr',
                                                                                       user_creation_email_pass[3])

        assert response.status_code == 500

        user_email_data = user_creation_email_pass[0]
        user_pass_data = user_creation_email_pass[1]
        user_token_data = user_creation_email_pass[3]
        user_delete_api.UserDelete.user_delete(self, user_email_data, user_pass_data, user_token_data)




