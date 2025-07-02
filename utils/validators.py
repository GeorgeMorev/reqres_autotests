import allure
from pydantic import ValidationError


def validate_with_pydantic(response, model):
    allure.attach(response.text, name="Raw Response", attachment_type=allure.attachment_type.JSON)
    """
    Валидация JSON-ответа с помощью Pydantic модели.
    При ошибке — прикрепляет ошибку в отчет Allure и выбрасывает исключение.
    """
    try:
        parsed_obj = model.parse_raw(response.text)
    except ValidationError as e:
        allure.attach(str(e), name="Pydantic Validation Error", attachment_type=allure.attachment_type.TEXT)
        raise

        # Если всё прошло успешно, логируем результат валидации
    allure.attach("Ответ успешно валидирован", name="Pydantic Validation", attachment_type=allure.attachment_type.TEXT)
    allure.attach(
        parsed_obj.model_dump_json(indent=2),
        name="Parsed Object",
        attachment_type=allure.attachment_type.JSON
    )