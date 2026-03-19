# API Tests (Pytest + Requests)

Набор тестов для проверки REST API.

## Стек технологий

* Python
* Pytest
* Requests
* Allure
* JSONSchema (валидация ответов)

## Будущая структура, если тестов станет больше

```
apiTesting/
├── tests/        # API тесты
├── schemas/      # JSON схемы для валидации
├── utils/        # Хелперы (клиенты, генераторы данных)
└── conftest.py   # Фикстуры (base_url, auth, setup)
```

## Особенности

* Тестирование REST API (CRUD операции)
* Валидация ответов через JSONSchema
* Переиспользуемые фикстуры (auth, headers, base_url)

## Покрытие

* Авторизация
* CRUD операции
* Проверка статусов и структуры ответа
* Негативные сценарии