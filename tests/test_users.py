import allure
import pytest
from api.endpoints import Endpoints
from utils.allure_logger import log_request, log_response
from utils.validators import validate_with_pydantic
from api.models.users import ListUsersResponse


@allure.epic("Users API")
@allure.feature("Получение списка пользователей")
class TestUsersAPI:
    @allure.title("Успешное получение списка пользователей")
    def test_get_list_users(self, client):
        with allure.step("Отправляем GET-запрос на список пользователей"):
            response = client.get(Endpoints.LIST_USERS)

        with allure.step("Проверяем статус-код ответа"):
            assert response.status_code == 200

        with allure.step("Валидация ответа с помощью Pydantic модели"):
            validate_with_pydantic(response, ListUsersResponse)

        # Логируем детали запроса и ответа для отчёта в Allure
        log_request(response)
        log_response(response)

    @pytest.mark.parametrize("page", [1, 2, 3, 4, 5])
    @allure.title("Проверка получения списка пользователей с пагинацией: страница {page}")
    def test_get_users_list_pagination(self, client, page):
        with allure.step(f"Отправляем GET-запрос на список пользователей с параметром page={page}"):
            response = client.get(Endpoints.LIST_USERS, params={"page": page})

        with allure.step("Проверяем, что статус-код ответа равен 200"):
            assert response.status_code == 200

        with allure.step("Проверяем, что в теле ответа есть поле 'data'"):
            data = response.json()
            assert "data" in data

        log_request(response)
        log_response(response)
