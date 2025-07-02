import allure
from utils.validators import validate_with_pydantic
from api.models.users import ListUsersResponse

import allure
from api.client import ReqresClient
from utils.allure_logger import log_request, log_response
from utils.validators import validate_with_pydantic
from api.models.users import ListUsersResponse


@allure.epic("Users API")
@allure.feature("Получение списка пользователей")
@allure.title("Успешное получение списка пользователей")
def test_get_list_users(client):
    with allure.step("Отправляем GET-запрос на список пользователей"):
        response = client.get_users_list()

    # Логируем детали запроса и ответа для отчёта в Allure
    log_request(response)
    log_response(response)

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200

    with allure.step("Валидация ответа с помощью Pydantic модели"):
        validate_with_pydantic(response, ListUsersResponse)
