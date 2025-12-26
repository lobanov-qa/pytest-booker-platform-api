import pytest

from clients.auth.auth_client import AuthClient
from clients.factories import  ClientFactory


@pytest.fixture
def authentication_client() -> AuthClient:
    return ClientFactory.get_auth_client()