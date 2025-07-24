# reqres_autotests

Автотесты для публичного REST API [Reqres.in](https://reqres.in), написанные с использованием `pytest`, `requests` и `Allure`.

## 🧪 Стек технологий

- Python 3.12  
- Pytest  
- Requests  
- Allure (отчетность)  
- GitHub Actions (CI)  
- Telegram Bot API (уведомления)  
- Pydantic (валидация ответов API)  


## 🚀 Запуск тестов

Локально:

```bash
pip install -r requirements.txt
pytest --alluredir=allure-results
allure serve allure-results

🧾 CI / CD

При каждом push в ветки main и develop:
	•	Запускаются все тесты
	•	Генерируется Allure-отчет
	•	При успехе отправляется уведомление в Telegram
	•	Отчёт публикуется через GitHub Pages

🔗 Allure-отчет

Открыть Allure-отчёт

📬 Telegram-уведомления

По завершении тестов бот отправляет сообщение с результатами в Telegram-чат.

🔧 Паттерны проектирования

В проекте применены следующие паттерны:
	•	Page Object (в API-интерпретации) — логика запросов и ответов вынесена в отдельные модули
	•	Data-driven testing — тесты параметризованы через фикстуры и @pytest.mark.parametrize
	•	Single Responsibility — строгое разделение ответственности между слоями: данные, логика, тесты
	•	Validation Layer — через Pydantic валидация схем ответов API

🧹 TODO
	•	Покрытие всех ручек
	•	Добавить негативные сценарии
	•	Подключить линтер и pre-commit
