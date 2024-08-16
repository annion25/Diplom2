import allure
import user_delete_api, user_creation_api, user_login_api


class TestUserLogin:

    @allure.title("Проверка успешной авторизации только что созданным пользователем")
    @allure.description("Авторизация только что созданным пользователем, проверка статуса ответа и тела ответа")
    def test_user_login_success(self):
        user_creation_data = user_creation_api.UserCreation.register_new_user_and_return_email_password(
            self, 10, 10, 10)
        user_creation_email_pass = user_creation_data[0]
        response = user_login_api.UserLogin.user_login(self, user_creation_email_pass[0], user_creation_email_pass[1])

        assert response.status_code == 200 and response.json()["success"] == True

        user_email_data = user_creation_email_pass[0]
        user_pass_data = user_creation_email_pass[1]
        user_token_data = user_creation_email_pass[3]
        user_delete_api.UserDelete.user_delete(self, user_email_data, user_pass_data, user_token_data)

    @allure.title("Проверка неуспешной авторизации")
    @allure.description("Авторизация с неправильной парол логин пароль, проверка статуса ответа и тела ответа")
    def test_user_non_existent_creds_fail(self):
        user_email = user_creation_api.UserCreation.generate_random_string(10)
        user_password = user_creation_api.UserCreation.generate_random_string(10)
        response = user_login_api.UserLogin.user_login(self, user_email, user_password)

        assert response.status_code == 401 and response.json()["success"] == False


