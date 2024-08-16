import requests
import allure
import urls

class UserChangeData:

    @allure.step("Отправка запроса на измененее данных")
    def user_change_data(self, token, email_new, name_new):
        payload = {
            "email": email_new,
            "name": name_new
        }
        return requests.patch(urls.BASE_URL + urls.USER_DELETE_UPDATE_URL, data=payload, headers={'Authorization': token})

