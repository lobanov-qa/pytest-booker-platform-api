from http import HTTPStatus

import httpx
import pytest

import allure
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.tags import AllureTag


SERVICES = [
    {"name": "auth", "port": 3004},
    {"name": "booking", "port": 3000},
    {"name": "branding", "port": 3002},
    {"name": "message", "port": 3006},
    {"name": "report", "port": 3005},
    {"name": "room", "port": 3001},
]


@pytest.mark.health
@allure.epic(AllureEpic.HEALTH)
@allure.feature(AllureFeature.CHECK_HEALTH)
@allure.tag(AllureTag.HEALTH)
class TestHealth:
    @pytest.mark.parametrize("service", SERVICES)
    @allure.story("Checking the server's health")
    def test_check_health(self, service: dict):
        name = service["name"]
        port = service["port"]
        url = f"http://localhost:{port}/{name}/actuator/health"

        try:
            response = httpx.get(url, timeout=10.0)
        except (httpx.ConnectError, httpx.TimeoutException) as e:
            pytest.fail(f"Failed to connect to service {name} on port {port}: {e}")

        assert response.status_code == HTTPStatus.OK, (
            f"Expected status 200, received{response.status_code}. URL: {url}"
        )

        try:
            data = response.json()
        except httpx.ResponseNotJSON:
            pytest.fail(
                pytest.fail(
                    f"Response is not JSON. Status: {response.status_code}, "
                    f"Body: {response.text}"
                )
            )

        assert data.get("status") == "UP", (
            f"Service {name} is not in UP state. Answer: {data}"
        )
