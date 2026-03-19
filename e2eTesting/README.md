# E2E Tests (Selenium + Pytest)

End-to-end тесты для проверки пользовательских сценариев

## Стек технологий

* Python
* Pytest
* Selenium WebDriver
* WebDriver Manager
* Allure (отчеты)
* Faker (генерация тестовых данных)


## Структура

```
e2eTesting/
├── pages/        # Page Object Model (страницы и бизнес-логика)
├── tests/        # Тестовые сценарии
├── utils/        # Вспомогательные утилиты (faker, data generators)
└── conftest.py   # Общие фикстуры (инициализация браузера)
```

## Особенности

* Используется **Page Object Model (POM)**
* Явные ожидания (`WebDriverWait`)
* Генерация тестовых данных через Faker
* Переиспользуемые фикстуры Pytest
