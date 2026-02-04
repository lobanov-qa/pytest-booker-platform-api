# 🚀 Pytest RESTful Booker Platform API Test Framework

## **[English](../../README.md)** | **Русский**


**Портфолио-фреймворк для автоматизации тестирования микросервисов [RESTful Booker Platform](https://github.com/mwinteringham/restful-booker-platform). Реализован на Python и Pytest с применением современных практик для улучшения читаемости и структуры кода.**

[![API tests](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/ci.yml/badge.svg)](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/ci.yml) [![Deploy docs](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/deploy-docs.yml)

## 🎯 **Цель проекта**

Этот проект создан в учебных целях для практического освоения следующих навыков:
- Автоматизация тестирования REST API на Python
- Работа с микросервисной архитектурой
- Организация кода тестов для удобства поддержки
- Интеграция с CI/CD (GitHub Actions) и системами отчетности (Allure)


## 💼 **Что реализовано в проекте**

- **Структурированная организация кода:** логическое разделение на клиенты API, фабрики данных и утилиты
- **Валидация ответов:** использование Pydantic моделей и JSON Schema для проверки структуры данных
- **Генерация тестовых данных:** применение библиотеки Faker для создания разнообразных входных данных
- **Подробная отчетность:** интеграция с Allure для наглядных отчетов о прохождении тестов
- **Автоматизация прогона:** настройка CI/CD пайплайна в GitHub Actions
- **Логирование:** кастомные обработчики в HTTPX для записи деталей запросов и ответов

## 💡 Пример теста: получение бронирования по ID

Ниже приведён пример теста с использованием Allure, Pydantic и кастомных фикстур:

```python
@allure.story(AllureStory.BOOKING_RETRIEVAL)
@allure.tag(AllureTag.GET_ENTITY)
@allure.severity(Severity.BLOCKER)
def test_get_booking_success(
    self,
    booking_private_client: PrivateBookingClient,
    created_booking: BookingFixture
):
    """
    Positive test: Retrieve specific booking by booking ID.
    Validates response matches the created booking data.
    """
    booking_id = created_booking.response.bookingid
    response = booking_private_client.get_booking_api(booking_id)
    allure.dynamic.title(f"GET /booking/{booking_id} - Retrieve specific booking by ID")
    
    assert_status_code(response.status_code, HTTPStatus.OK)
    response_data = BookingSchema.model_validate_json(response.text)
    validate_json_schema(response.json(), response_data.model_json_schema())
    assert_get_booking_response(response_data, created_booking.response.booking)
```


<img width="774" height="890" alt="Image" src="https://github.com/user-attachments/assets/b280e5ab-d742-4582-a392-15157f923e0f" />


## 🛠 **Стек технологий**

| Категория | Инструменты |
|-----------|-------------|
| **Фреймворк** | Python 3.11+, Pytest |
| **HTTP клиент** | HTTPX (с логированием через кастомные обработчики) |
| **Валидация** | Pydantic, JSON Schema |
| **Тестовые данные** | Faker |
| **Отчетность** | Allure-pytest, Swagger Coverage Tool |
| **Автоматизация** | GitHub Actions, Docker Compose |




## 📊 **[Единый портал отчетов на GitHub Pages](https://lobanov-qa.github.io/pytest-booker-platform-api/)**

- **Allure 3 отчеты**: интерактивные результаты тестов с историей запусков
- **Покрытие API**: метрики валидации Swagger спецификаций
- **Документация**: живая документация на основе OpenAPI

![Image](https://github.com/user-attachments/assets/9b5b8203-bfe1-43f1-9d40-61b1ac0fad32)

---
# 🚀 **Быстрый старт**

### Предварительные требования
- Python 3.11 или выше
- Docker & Docker Compose
- Git

> ⚠️ **Важно:** проект тестирует учебную микросервисную платформу RESTful Booker Platform, развертываемую через Docker Compose.
---
##  Установка и настройка

### 1. Запустите целевые микросервисы
```bash
git clone https://github.com/mwinteringham/restful-booker-platform.git
cd restful-booker-platform
docker compose up -d
```

### 2. Установите тестовый фреймворк
```bash
cd ..
git clone https://github.com/lobanov-qa/pytest-booker-platform-api.git
cd pytest-booker-platform-api
```

### 3. Создайте виртуальное окружение
**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Установите зависимости
```bash
pip install -e .
```

### 5. Настройте окружение
```bash
cp .env.example .env
```
Отредактируйте файл `.env` вручную, указав ваши настройки.

### 6. Запустите тесты
```bash
python scripts/wait_for_services.py
pytest tests/ --alluredir=allure-results -v
```

### 7. Посмотрите отчет
```bash
allure serve allure-results
```

Эта команда откроет отчёт Allure в вашем браузере по умолчанию.

## 📁 **Структура проекта**
```
pytest-booker-platform-api/
├── src/
│   ├── clients/                    # Доменно-ориентированные API клиенты
│   │   ├── auth/                   # Клиент сервиса аутентификации
│   │   │   ├── auth_client.py      # Публичные/приватные методы клиента с Allure шагами
│   │   │   ├── routes.py           # Определения API эндпоинтов и URL константы
│   │   │   └── auth_schema.py      # Pydantic модели для запросов/ответов Auth API
│   │   ├── booking/                # Клиент сервиса бронирования (структура аналогична auth)
│   │   ├── api_client.py           # Базовый HTTP клиент с декораторами Allure шагов
│   │   ├── api_coverage.py         # Декораторы отслеживания покрытия Swagger
│   │   ├── event_hooks.py          # HTTPX event hooks для логирования запросов/ответов
│   │   └── factories.py            # Фабрика клиентов для легкого создания экземпляров
│   ├── data_factories/             # Фабричный паттерн для генерации тестовых данных
│   │   ├── booking_factory.py      # Фабричные методы для тестовых данных бронирования
│   │   └── query_factories.py      # Фабричные методы для параметров запросов
│   └── utils/
│       ├── allure/                 # Конфигурация и декораторы Allure
│       ├── assertions/             # Кастомные библиотеки ассертов
│       │   ├── base.py             # Базовые утилиты ассертов
│       │   └── schema.py           # Ассерты валидации JSON Schema
│       ├── http/curl.py            # Утилиты генерации CURL команд
│       ├── fakers.py               # Расширенные утилиты Faker для тестовых данных
│       └── logger.py               # Конфигурация структурированного логирования
├── tests/
│   ├── auth/                       # Тестовые наборы аутентификации
│   │   └── test_authentication.py  # Тесты Auth API с параметризацией
│   ├── booking/                    # Тестовые наборы сервиса бронирования
│   └── test_api_health.py          # Проверки здоровья всех сервисов
├── fixtures/                       # Pytest фикстуры
│   ├── auth.py                     # Фикстуры, связанные с аутентификацией
│   └── allure.py                   # Фикстуры отчетности Allure
├── scripts/                        # Утилитарные скрипты
│   └── wait_for_services.py        # Утилиты проверки здоровья сервисов
└── .github/workflows/              # CI/CD пайплайны
│   ├── ci.yml                      # Основной workflow тестирования
│   └── deploy-docs.yml             # Workflow деплоя документации
```
## 📚 Приобретённые навыки

На примере этого проекта я освоил:

- **Python / Pytest**: написание параметризованных тестов, использование фикстур, организацию модульной структуры.
- **Работа с API**: отправка запросов (HTTPX), обработка авторизации, валидация ответов.
- **Организация кода**: применение принципов SOLID и domain-oriented подхода для разделения ответственности.
- **Инструменты автоматизации**: настройка GitHub Actions, генерация отчётов Allure, интеграция с Swagger.
- **Документирование**: ведение README, настройка публикации документации через GitHub Pages.
- **Анализ качества**: отслеживание покрытия API по OpenAPI-спецификациям.

Проект стал для меня "полигоном" для экспериментов с лучшими практиками, которые я хочу развивать в профессиональной среде.


## 📞 **Контакты**

Готов к код-ревью, обсуждению решений и обратной связи.  
Ищу возможность начать карьеру в качестве **инженера AQA**, чтобы расти в команде и вносить вклад в качество ПО.

- **GitHub**: [lobanov-qa](https://github.com/lobanov-qa)
- **Telegram**: [lobanov_e_i](https://t.me/lobanov_e_i)
- **LinkedIn**: [evgenii-lobanov-qa](https://www.linkedin.com/in/evgenii-lobanov-qa/)