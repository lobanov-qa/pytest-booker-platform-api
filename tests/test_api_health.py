import httpx
import pytest
from http import HTTPStatus

SERVICES = [
    {"name": "auth", "port": 3004},
    {"name": "booking", "port": 3000},
    {"name": "branding", "port": 3002},
    {"name": "message", "port": 3006},
    {"name": "report", "port": 3005},
    {"name": "room", "port": 3001},
]

class TestHealth:
    @pytest.mark.parametrize("service", SERVICES)
    def test_check_health(self, service: dict):
        name = service["name"]
        port = service["port"]
        url = f"http://localhost:{port}/{name}/actuator/health"

        try:
            response = httpx.get(url, timeout=10.0)
        except (httpx.ConnectError, httpx.TimeoutException) as e:
            pytest.fail(f"Не удалось подключиться к сервису {name} на порту {port}: {e}")

        assert response.status_code == HTTPStatus.OK, (
            f"Ожидался статус 200, получено {response.status_code}. URL: {url}"
        )

        try:
            data = response.json()
        except httpx.ResponseNotJSON:
            pytest.fail(f"Ответ не в формате JSON. Статус: {response.status_code}, Тело: {response.text}")

        assert data.get("status") == "UP", (
            f"Сервис {name} не в состоянии UP. Ответ: {data}"
        )
 
