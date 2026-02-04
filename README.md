# 🚀 Pytest RESTful Booker Platform API Test Framework

## **English** | **[Русский](docs/readme/README_RU.md)**

**Portfolio framework for automated testing of [RESTful Booker Platform](https://github.com/mwinteringham/restful-booker-platform) microservices. Implemented in Python and Pytest using modern practices to improve code readability and structure.**

[![API tests](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/ci.yml/badge.svg)](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/ci.yml) [![Deploy docs](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/lobanov-qa/pytest-booker-platform-api/actions/workflows/deploy-docs.yml)

## 🎯 **Project Purpose**

This project was created for educational purposes to practically master the following skills:
- Automated testing of REST APIs in Python
- Working with microservice architecture
- Organizing test code for maintainability
- Integration with CI/CD (GitHub Actions) and reporting systems (Allure)

## 💼 **What's Implemented in the Project**

- **Structured code organization:** logical separation into API clients, data factories, and utilities
- **Response validation:** using Pydantic models and JSON Schema to verify data structure
- **Test data generation:** using the Faker library to create diverse input data
- **Detailed reporting:** integration with Allure for clear test execution reports
- **Automated test runs:** configuring CI/CD pipeline in GitHub Actions
- **Logging:** custom handlers in HTTPX for recording request and response details

## 💡 Test Example: Retrieving Booking by ID

Below is an example test using Allure, Pydantic, and custom fixtures:

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

## 🛠 **Technology Stack**

| Category | Tools |
|----------|-------|
| **Framework** | Python 3.11+, Pytest |
| **HTTP Client** | HTTPX (with logging via custom handlers) |
| **Validation** | Pydantic, JSON Schema |
| **Test Data** | Faker |
| **Reporting** | Allure-pytest, Swagger Coverage Tool |
| **Automation** | GitHub Actions, Docker Compose |

## 📊 **[Unified Reporting Portal on GitHub Pages](https://lobanov-qa.github.io/pytest-booker-platform-api/)**

- **Allure 3 Reports:** interactive test results with run history
- **API Coverage:** Swagger specification validation metrics
- **Documentation:** live documentation based on OpenAPI

![Image](https://github.com/user-attachments/assets/9b5b8203-bfe1-43f1-9d40-61b1ac0fad32)

---
# 🚀 **Quick Start**

### Prerequisites
- Python 3.11 or higher
- Docker & Docker Compose
- Git

> ⚠️ **Important:** the project tests the educational RESTful Booker Platform microservices, deployed via Docker Compose.

---
## Installation and Setup

### 1. Start the Target Microservices
```bash
git clone https://github.com/mwinteringham/restful-booker-platform.git
cd restful-booker-platform
docker compose up -d
```

### 2. Install the Test Framework
```bash
cd ..
git clone https://github.com/lobanov-qa/pytest-booker-platform-api.git
cd pytest-booker-platform-api
```

### 3. Create a Virtual Environment
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

### 4. Install Dependencies
```bash
pip install -e .
```

### 5. Configure Environment
```bash
cp .env.example .env
```
Edit the `.env` file manually with your settings.

### 6. Run Tests
```bash
python scripts/wait_for_services.py
pytest tests/ --alluredir=allure-results -v
```

### 7. View Report
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
├── fixtures/                       # Pytest fixtures
│   ├── auth.py                     # Authentication-related fixtures
│   └── allure.py                   # Allure reporting fixtures
├── scripts/                        # Utility scripts
│   └── wait_for_services.py        # Service health check utilities
└── .github/workflows/              # CI/CD pipelines
│   ├── ci.yml                      # Main testing workflow
│   └── deploy-docs.yml             # Documentation deployment workflow
```

## 📚 **Skills Acquired**

Through this project, I have mastered:

- **Python / Pytest:** writing parameterized tests, using fixtures, organizing modular structure.
- **Working with APIs:** sending requests (HTTPX), handling authorization, validating responses.
- **Code organization:** applying SOLID principles and domain-oriented approach for separation of concerns.
- **Automation tools:** configuring GitHub Actions, generating Allure reports, integrating with Swagger.
- **Documentation:** maintaining README, setting up documentation publishing via GitHub Pages.
- **Quality analysis:** tracking API coverage against OpenAPI specifications.

This project has served as a "testing ground" for experimenting with best practices that I want to develop in a professional environment.

## 📞 **Contacts**

Ready for code reviews, discussion of solutions, and feedback.  
Looking for an opportunity to start a career as an **AQA Engineer** to grow within a team and contribute to software quality.

- **GitHub:** [lobanov-qa](https://github.com/lobanov-qa)
- **Telegram:** [lobanov_e_i](https://t.me/lobanov_e_i)
- **LinkedIn:** [evgenii-lobanov-qa](https://www.linkedin.com/in/evgenii-lobanov-qa/)
```