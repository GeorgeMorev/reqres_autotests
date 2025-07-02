import allure
from api.client import ReqresClient


@allure.epic("Users API")
@allure.feature("Получение списка пользователей")
@allure.title("Успешное получение списка пользователей")
def test_get_list_users(client):
    with allure.step("Отправляем GET-запрос на список пользователей"):
        response = client.get_users_list()

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200

    with allure.step("Проверяем, что в теле ответа есть поле 'data'"):
        data = response.json()
        assert "data" in data
