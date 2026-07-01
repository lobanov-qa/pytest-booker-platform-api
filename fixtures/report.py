import pytest

from httpx import Cookies

from clients.report.public_report_client import PublicReportClient
from clients.report.private_report_client import PrivateReportClient
from clients.client_factories import ClientFactory


@pytest.fixture
def report_public_client() -> PublicReportClient:
    """Fixture providing an unauthenticated PublicReportClient."""
    client = ClientFactory.get_public_report_client()
    yield client
    client.close()


@pytest.fixture
def report_private_client(auth_cookies: Cookies) -> PrivateReportClient:
    """Fixture providing an authenticated PrivateReportClient."""
    client = ClientFactory.get_private_report_client(auth_cookies)
    yield client
    client.close()


@pytest.fixture
def report_private_client_invalid(invalid_cookies: Cookies) -> PrivateReportClient:
    """PrivateReportClient with invalid cookies for negative tests."""
    client = ClientFactory.get_private_report_client(invalid_cookies)
    yield client
    client.close()
