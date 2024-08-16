import urls
import requests
import random
import string
import allure

class UserCreation:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step("Отправляем запрос на создание пользователя")
    def register_new_user_and_return_email_password(self, email_length, pass_length, name_length):
        email_pass = []
        email = UserCreation.generate_random_string(email_length) + '@ya.ru'
        password = UserCreation.generate_random_string(pass_length)
        name = UserCreation.generate_random_string(name_length)
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(urls.BASE_URL + urls.USER_CREATION_URL, data=payload)
        if response.status_code == 200:
            email_pass.append(email)
            email_pass.append(password)
            email_pass.append(name)
            r = response.json()
            email_pass.append(r["accessToken"])
        return email_pass, response

    def register_user_with_given_data_and_return_response(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(urls.BASE_URL + urls.USER_CREATION_URL, data=payload)
        return response

