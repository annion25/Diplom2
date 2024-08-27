import allure
import requests
import urls

class GetUserOrders:

    @allure.step("Отправляем запрос на получение заказов пользователя")
    def get_users_orders(self, token):
        return requests.get(urls.BASE_URL + urls.ORDER_API, headers={'Authorization': token})

