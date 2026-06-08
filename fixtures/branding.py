import pytest

from httpx import Cookies

from clients.branding.branding_schema import BrandingSchema
from clients.branding.public_branding_client import PublicBrandingClient
from clients.branding.private_branding_client import PrivateBrandingClient
from clients.client_factories import ClientFactory
from data_factories.branding_factory import BrandingFactory


@pytest.fixture
def public_branding_client() -> PublicBrandingClient:
    """PublicBrandingClient for accessing public branding endpoints."""
    client = ClientFactory.get_public_branding_client()
    yield client
    client.close()


@pytest.fixture
def private_branding_client(auth_cookies: Cookies) -> PrivateBrandingClient:
    """PrivateBrandingClient with valid authentication cookies."""
    client = ClientFactory.get_private_branding_client(auth_cookies)
    yield client
    client.close()


@pytest.fixture
def private_branding_client_invalid(invalid_cookies: Cookies) -> PrivateBrandingClient:
    """PrivateBrandingClient with invalid cookies for negative auth tests."""
    client = ClientFactory.get_private_branding_client(invalid_cookies)
    yield client
    client.close()


@pytest.fixture
def valid_branding_update() -> BrandingSchema:
    """Valid branding data with randomized values for PUT /branding/."""
    return BrandingFactory.build()


@pytest.fixture
def current_branding(public_branding_client: PublicBrandingClient) -> BrandingSchema:
    """Retrieves the current branding state for comparison in update tests."""
    return public_branding_client.get_branding()