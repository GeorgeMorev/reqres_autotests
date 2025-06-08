# Reqres Autotests (https://reqres.in/)

Pet-проект по автоматизации API-тестирования с использованием [https://reqres.in](https://reqres.in).

## Цель

- Изучение автоматизации тестирования API на Python
- Практика работы с Pytest, Requests, Allure
- Имитация рабочего процесса: структура, ветвление, фиксация зависимостей, CI (в перспективе)

## Технологии

- Python 3.12
- unittest
- pytest
- requests
- allure

## Установка

Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv venv
source venv/bin/activate  # или .\venv\Scripts\activate в Windows
pip install -r requirements.txt
```

## TODO

- [ ] Настроить структуру проекта
- [ ] Написать первые тесты (авторизация)
- [ ] Добавить `requirements.txt`
- [ ] Настроить отчётность через Allure
