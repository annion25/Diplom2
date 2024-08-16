import allure
import user_delete_api, user_creation_api


class TestUserCreation:

    @allure.title("Проверка успешного создания пользователя")
    @allure.description("Создание пользователя с рандомными логином, паролем, именем, проверка статуса ответа и тела ответа")
    def test_user_creation_success(self):
        user_creation_data = user_creation_api.UserCreation.register_new_user_and_return_email_password(
            self, 10, 10, 10)
        user_creation_request = user_creation_data[1]
        user_creation_email_pass = user_creation_data[0]

        assert user_creation_request.status_code == 200 and user_creation_request.json()["success"] == True

        user_email_data = user_creation_email_pass[0]
        user_pass_data = user_creation_email_pass[1]
        user_token_data = user_creation_email_pass[3]
        user_delete_api.UserDelete.user_delete(self, user_email_data, user_pass_data, user_token_data)

    @allure.title("Проверка создания пользователя с существующими данными")
    @allure.description(
        "Создание пользователя с уже существущими логином, паролем, именем, проверка статуса ответа и тела ответа")
    def test_user_creation_already_registered_fail(self):
        user_creation_data = user_creation_api.UserCreation.register_new_user_and_return_email_password(
            self, 10, 10, 10)
        user_creation_email_pass = user_creation_data[0]
        user_creation_data_double = user_creation_api.UserCreation.register_user_with_given_data_and_return_response(
            self, user_creation_email_pass[0], user_creation_email_pass[1], user_creation_email_pass[2])

        assert user_creation_data_double.status_code == 403 and user_creation_data_double.json()["success"] == False

        user_email_data = user_creation_email_pass[0]
        user_pass_data = user_creation_email_pass[1]
        user_token_data = user_creation_email_pass[3]
        user_delete_api.UserDelete.user_delete(self, user_email_data, user_pass_data, user_token_data)

    @allure.title("Проверка создания пользователя с незаполненным именем")
    @allure.description(
        "Создание пользователя с незаполненным именем")
    def test_user_creation_no_name_fail(self):
        user_creation_data = user_creation_api.UserCreation.register_new_user_and_return_email_password(
            self, 10, 10, 0)
        user_creation_request = user_creation_data[1]

        assert user_creation_request.status_code == 403 and user_creation_request.json()["success"] == False

