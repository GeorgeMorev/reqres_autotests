import allure
from pydantic import ValidationError


def validate_with_pydantic(response, model):
    """
    Валидация JSON-ответа с помощью Pydantic модели.
    При ошибке — прикрепляет ошибку в отчет Allure и выбрасывает исключение.
    """
    try:
        # Парсим тело ответа через Pydantic модель
        model.parse_raw(response.text)
    except ValidationError as e:
        # Добавляем в отчет Allure подробности ошибки валидации
        allure.attach(str(e), name="ValidationError", attachment_type=allure.attachment_type.TEXT)
        raise
