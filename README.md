# 🚀 Pytest RESTful Booker Platform API Test Framework

**A framework for testing microservices platform [RESTful Booker Platform](https://github.com/mwinteringham/restful-booker-platform),, demonstrating modern automation approaches with a focus on maintainability and scalability.**

[![API tests](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/ci.yml/badge.svg)](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/ci.yml)

## **English** | **[Русский](docs/readme/README_RU.md)**

## 💼 **Key Features**

- **Application of design patterns** in testing
- **Domain-oriented API clients** with clear separation of responsibilities
- **Factory pattern** for test data generation using Faker
- **Multi-level validation**: Pydantic models + JSON Schema
- **Integrated reporting**: Allure 3 + Swagger Coverage + Zudoku documentation
- **Automatic CURL command generation** for debugging
- **Custom HTTPX hooks** for request/response logging
- **CI/CD pipeline setup** with GitHub Actions

## 🛠 **Technology Stack**

| Category | Tools |
|-----------|-------------|
| **Framework** | Python 3.11+, Pytest |
| **HTTP Client** | HTTPX with custom hooks |
| **Validation** | Pydantic, JSON Schema |
| **Test Data** | Faker (factory pattern) |
| **Reporting** | Allure-pytest, Swagger Coverage |
| **CI/CD** | GitHub Actions, Docker |

## 📊 **[Unified Reporting Portal on GitHub Pages](https://lobanov-qa.github.io/pytest-booker-platform-api/)**

- **Allure Reports**: Interactive test results with trends
- **API Coverage**: Swagger specification validation metrics
- **Documentation**: Live documentation based on OpenAPI

![Image](https://github.com/user-attachments/assets/9b5b8203-bfe1-43f1-9d40-61b1ac0fad32)

---
# 🚀 **Quick Start**

### Prerequisites
- Python 3.11 or higher
- Docker & Docker Compose
- Git

---
## Installation and Setup

### Clone and run target microservices
```bash
git clone https://github.com/mwinteringham/restful-booker-platform.git
cd restful-booker-platform
docker compose up -d
cd ..
```

### Clone the test framework repository
```bash
# Clone the repository
git clone https://github.com/lobanov-qa/pytest-booker-platform-api.git
cd pytest-booker-platform-api
```

### Create a virtual environment

It is recommended to use a virtual environment for managing project dependencies. Follow the instructions for your operating system:

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

### Install dependencies (from pyproject.toml)
```bash
pip install -e .
```

### Copy environment configuration
```bash
cp .env.example .env
```

### Edit .env with your service URLs and credentials
```bash
# Wait for services to become healthy
python ../scripts/wait_for_services.py

# Run all tests with Allure reporting
pytest tests/ --alluredir=allure-results -v

# Generate and view Allure report
allure serve allure-results
```

### View Allure 2 Report

After running the tests, you can generate and view the Allure report using:

```bash
allure serve allure-results
```

This command will open the Allure report in your default browser.

## 📁 **Project Structure**
```
pytest-booker-platform-api/
├── src/
│   ├── clients/                    # Domain-oriented API clients
│   │   ├── auth/                   # Authentication service client
│   │   │   ├── auth_client.py      # Public/private client methods with Allure steps
│   │   │   ├── routes.py           # API endpoint definitions and URL constants
│   │   │   └── auth_schema.py      # Pydantic models for Auth API requests/responses
│   │   ├── booking/                # Booking service client (structure similar to auth)
│   │   ├── api_client.py           # Base HTTP client with Allure step decorators
│   │   ├── api_coverage.py         # Swagger coverage tracking decorators
│   │   ├── event_hooks.py          # HTTPX event hooks for request/response logging
│   │   └── factories.py            # Client factory for easy instance creation
│   ├── data_factories/             # Factory pattern for test data generation
│   │   ├── booking_factory.py      # Factory methods for booking test data
│   │   └── query_factories.py      # Factory methods for query parameters
│   └── utils/
│       ├── allure/                 # Allure configuration and decorators
│       │   ├── epics.py            # Allure epics definitions
│       │   ├── features.py         # Allure features definitions
│       │   ├── stories.py          # Allure stories definitions
│       │   ├── tags.py             # Allure tags definitions
│       │   └── environment.py      # Allure environment configuration
│       ├── assertions/             # Custom assertion libraries
│       │   ├── base.py             # Basic assertion utilities
│       │   └── schema.py           # JSON Schema validation assertions
│       ├── http/curl.py            # CURL command generation utilities
│       ├── fakers.py               # Extended Faker utilities for test data
│       └── logger.py               # Structured logging configuration
├── tests/
│   ├── auth/                       # Authentication test suites
│   │   └── test_authentication.py  # Auth API tests with parameterization
│   ├── booking/                    # Booking service test suites
│   └── test_api_health.py          # Health checks for all services
├── docs/zudoku/                    # Interactive API documentation (Zudoku)
│   ├── apis/                       # OpenAPI/Swagger specifications
│   ├── pages/                      # Documentation pages
│   └── scripts/                    # Documentation generation scripts
├── fixtures/                       # Pytest fixtures
│   ├── auth.py                     # Authentication-related fixtures
│   └── allure.py                   # Allure reporting fixtures
├── scripts/                        # Utility scripts
│   └── wait_for_services.py        # Service health check utilities
└── .github/workflows/              # CI/CD pipelines
│   ├── ci.yml                      # Main testing workflow
│   └── deploy-docs.yml             # Documentation deployment workflow
```

## 📞 **Contacts**

- **GitHub**: [lobanov-qa](https://github.com/lobanov-qa)
- **Telegram**: [lobanov_e_i](https://t.me/lobanov_e_i)
- **LinkedIn**: [evgenii-lobanov-qa](https://www.linkedin.com/in/evgenii-lobanov-qa/)
```
