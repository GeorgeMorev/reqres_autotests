import allure
from utils.validators import validate_with_pydantic
from api.models.users import ListUsersResponse


@allure.epic("Users API")
@allure.feature("Получение списка пользователей")
@allure.title("Успешное получение списка пользователей")
def test_get_list_users(client):
    with allure.step("Отправляем GET-запрос на список пользователей"):
        response = client.get_users_list()

    with allure.step("Логируем URL запроса"):
        allure.attach(response.request.url, name="Request URL", attachment_type=allure.attachment_type.URI_LIST)

    with allure.step("Логируем HTTP-метод запроса"):
        allure.attach(response.request.method, name="Request Method", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Логируем заголовки запроса"):
        headers = response.request.headers
        headers_str = "\n".join(f"{k}: {v}" for k, v in headers.items())
        allure.attach(headers_str, name="Request Headers", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Логируем тело запроса"):
        body = response.request.body
        if body:
            allure.attach(body if isinstance(body, str) else body.decode('utf-8'),
                          name="Request Body", attachment_type=allure.attachment_type.JSON)
        else:
            allure.attach("No request body", name="Request Body", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Логируем заголовки ответа"):
        headers = response.headers
        headers_str = "\n".join(f"{k}: {v}" for k, v in headers.items())
        allure.attach(headers_str, name="Response Headers", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Логируем тело ответа"):
        allure.attach(
            response.text,
            name="Response body",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Логируем время ответа"):
        response_time_ms = response.elapsed.total_seconds() * 1000  # в миллисекундах
        allure.attach(f"{response_time_ms:.2f} ms", name="Response Time", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Логируем статус-код ответа"):
        allure.attach(str(response.status_code), name="Response status code",
                      attachment_type=allure.attachment_type.TEXT)

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200

    with allure.step("Валидация ответа с помощью Pydantic модели"):
        validate_with_pydantic(response, ListUsersResponse)
