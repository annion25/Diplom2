import requests
import allure
import urls


class UserDelete:

    @allure.step("Отправка запроса на удаление пользователя")
    def user_delete(self, email, password, token):
        payload = {
            "email": email,
            "password": password
        }
        return requests.delete(urls.BASE_URL + urls.USER_DELETE_UPDATE_URL, data=payload, headers={'Authorization': token})

