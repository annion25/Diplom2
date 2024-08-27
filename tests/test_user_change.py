import allure
from user_login_api import UserLogin
from user_creation_api import UserCreation
from user_delete_api import UserDelete
from user_change_api import UserChangeData


class TestUserChangeData:

    @allure.title("Проверка возможность изменения полей у только созданного авторизованного пользователя")
    @allure.description("Изменение почты и имени у только что созданного пользователя, проверка статуса ответа и тела ответа")
    def test_user_change_data_success(self):
        user_creation_data = UserCreation.register_new_user_and_return_email_password(
            self, 10, 10, 10)
        user_creation_email_pass = user_creation_data[0]
        response_login = UserLogin.user_login(self, user_creation_email_pass[0], user_creation_email_pass[1])
        new_email = UserCreation.generate_random_string(10) + '@ya.ru'
        new_name = UserCreation.generate_random_string(10)
        response_change = UserChangeData.user_change_data(self, response_login.json()["accessToken"], new_email, new_name)

        assert response_change.status_code == 200 and response_change.json()["success"] == True

        user_email_data = user_creation_email_pass[0]
        user_pass_data = user_creation_email_pass[1]
        user_token_data = user_creation_email_pass[3]
        UserDelete.user_delete(self, user_email_data, user_pass_data, user_token_data)


    @allure.title("Проверка невозможности изменения полей у только созданного пользователя без авторизации")
    @allure.description(
        "Изменение почты и имени у только что созданного пользователя без передачи токена при изменении данных, проверка статуса ответа и тела ответа")
    def test_user_change_data_unloged_fail(self):
        user_creation_data = UserCreation.register_new_user_and_return_email_password(
            self, 10, 10, 10)
        user_creation_email_pass = user_creation_data[0]
        UserLogin.user_login(self, user_creation_email_pass[0], user_creation_email_pass[1])
        new_email = UserCreation.generate_random_string(10) + '@ya.ru'
        new_name = UserCreation.generate_random_string(10)
        response_change = UserChangeData.user_change_data(self, "",
                                                                               new_email, new_name)

        assert response_change.status_code == 401 and response_change.json()["success"] == False

        user_email_data = user_creation_email_pass[0]
        user_pass_data = user_creation_email_pass[1]
        user_token_data = user_creation_email_pass[3]
        UserDelete.user_delete(self, user_email_data, user_pass_data, user_token_data)

