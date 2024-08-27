import requests
import allure
import urls

class OrderCreation:

    @allure.step("Отправка запроса на создание заказа")
    def order_creation(self, body, token):

        return requests.post(urls.BASE_URL + urls.ORDER_API, json={"ingredients": body}, headers={'Authorization': token})

    @allure.step("Отправка запроса на получение ингредиентов, набор списка ингредиентов для бургера")
    def order_some_ingredients_get(self):
        response = requests.get(urls.BASE_URL + urls.INGREDIENTS_API)
        r = response.json()
        ingredients = [r['data'][0]['_id'], r['data'][1]['_id'], r['data'][4]['_id']]
        return ingredients




