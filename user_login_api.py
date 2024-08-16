import requests
import allure
import urls


class UserLogin:

    @allure.step("Отправка запроса на авторизацию")
    def user_login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        return requests.post(urls.BASE_URL + urls.USER_LOGIN_URL, data=payload)

