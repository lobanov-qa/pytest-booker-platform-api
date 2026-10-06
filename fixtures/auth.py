import pytest
from httpx import Cookies

from clients.auth.auth_client import AuthClient
from clients.auth.auth_schema import LoginRequestSchema
from clients.client_factories import ClientFactory


@pytest.fixture
def authentication_client() -> AuthClient:
    return ClientFactory.get_auth_client()


@pytest.fixture
def auth_cookies(authentication_client: AuthClient) -> Cookies:
    login_request = LoginRequestSchema()
    response = authentication_client.login_api(login_request)
    cookies: Cookies = response.cookies
    return cookies


@pytest.fixture
def invalid_cookies() -> Cookies:
    """Фикстура с невалидными cookies для негативных тестов."""
    cookies = Cookies()
    cookies.set("token", "invalid_token_value")
    return cookies
