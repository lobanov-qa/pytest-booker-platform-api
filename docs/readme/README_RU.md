# 🚀 Pytest RESTful Booker Platform API Test Framework

**Фреймворк для тестирования микросервисной платформы [RESTful Booker Platform](https://github.com/mwinteringham/restful-booker-platform), демонстрирующий современные подходы к автоматизации с акцентом на поддерживаемость и масштабируемость.**


[![API tests](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/ci.yml/badge.svg)](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/ci.yml)

## **[English](../../README.md)** | **Русский**

## 💼 **Ключевые особенности**

- **Применение паттернов проектирования** в тестировании
- **Доменно-ориентированные API клиенты**  с четким разделением ответственности
- **Factory паттерн** для генерации тестовых данных через Faker
- **Многоуровневая валидация**: Pydantic модели + JSON Schema
- **Интегрированная отчетность**: Allure 3 + Swagger Coverage + Zudoku документация
- **Автоматическая генерация CURL команд** для отладки
- **Кастомные HTTPX хуки** для логирования запросов/ответов
- **Настройка CI/CD пайплайнов** GitHub Actions


## 🛠 **Стек технологий**

| Категория | Инструменты |
|-----------|-------------|
| **Фреймворк** | Python 3.11+, Pytest |
| **HTTP клиент** | HTTPX с кастомными hooks |
| **Валидация** | Pydantic, JSON Schema |
| **Тестовые данные** | Faker (фабричный паттерн) |
| **Отчетность** | Allure-pytest, Swagger Coverage |
| **CI/CD** | GitHub Actions, Docker |


## 📊 **[Единый портал отчетов на GitHub Pages](https://lobanov-qa.github.io/pytest-booker-platform-api/)**

- **Allure отчеты**: интерактивные результаты тестов с трендами
- **Покрытие API**: метрики валидации Swagger спецификаций
- **Документация**: живая документация на основе OpenAPI

![Image](https://github.com/user-attachments/assets/9b5b8203-bfe1-43f1-9d40-61b1ac0fad32)

---
# 🚀 **Быстрый старт**

### Предварительные требования
- Python 3.11 или выше
- Docker & Docker Compose
- Git


---
## Установка и настройка

### Клонировать и запустить целевые микросервисы
```bash
git clone https://github.com/mwinteringham/restful-booker-platform.git
cd restful-booker-platform
docker compose up -d
cd ..
```

### Клонировать репозиторий тестового фреймворка
```bash
# Клонировать репозиторий
git clone https://github.com/lobanov-qa/pytest-booker-platform-api.git
cd pytest-booker-platform-api
```

### Создайте виртуальную среду

Для управления зависимостями проекта рекомендуется использовать виртуальную среду. Следуйте инструкциям для вашей операционной системы:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Установить зависимости (из pyproject.toml)
```bash
pip install -e .
```

### Скопировать конфигурацию окружения
```bash
cp .env.example .env
```
### Отредактировать .env с вашими URL сервисов и учетными данными
```bash
# Подождать, пока сервисы станут здоровыми
python ../scripts/wait_for_services.py

# Запустить все тесты с отчетностью Allure
pytest tests/ --alluredir=allure-results -v

# Сгенерировать и посмотреть отчет Allure
allure serve allure-results
```


### Просмотр отчёта Allure 2

После выполнения тестов вы можете создать и просмотреть отчёт Allure с помощью:

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
│       │   ├── epics.py            # Определения Allure epics
│       │   ├── features.py         # Определения Allure features
│       │   ├── stories.py          # Определения Allure stories
│       │   ├── tags.py             # Определения Allure tags
│       │   └── environment.py      # Конфигурация окружения Allure
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
├── docs/zudoku/                    # Интерактивная документация API (Zudoku)
│   ├── apis/                       # OpenAPI/Swagger спецификации
│   ├── pages/                      # Страницы документации
│   └── scripts/                    # Скрипты генерации документации
├── fixtures/                       # Pytest фикстуры
│   ├── auth.py                     # Фикстуры, связанные с аутентификацией
│   └── allure.py                   # Фикстуры отчетности Allure
├── scripts/                        # Утилитарные скрипты
│   └── wait_for_services.py        # Утилиты проверки здоровья сервисов
└── .github/workflows/              # CI/CD пайплайны
│   ├── ci.yml                      # Основной workflow тестирования
│   └── deploy-docs.yml             # Workflow деплоя документации
```

## 📞 **Контакты**

- **GitHub**: [lobanov-qa](https://github.com/lobanov-qa)
- **Telegram**: [lobanov_e_i](https://t.me/lobanov_e_i)
- **LinkedIn**: [evgenii-lobanov-qa](https://www.linkedin.com/in/evgenii-lobanov-qa/)