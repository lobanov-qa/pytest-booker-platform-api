import pytest

from pydantic import BaseModel
from httpx import Cookies

from clients.booking.booking_schema import CreateBookingRequestSchema, CreateBookingResponseSchema
from clients.booking.private_booking_client import PrivateBookingClient
from clients.booking.public_booking_client import PublicBookingClient
from config import settings
from src.clients.client_factories import ClientFactory
from src.data_factories.booking_factory import CreateBookingRequestFactory


class BookingFixture(BaseModel):
    """
    Booking context - used to pass data between tests and validation.
    """
    request: CreateBookingRequestSchema
    response: CreateBookingResponseSchema

    @property
    def booking_id(self) -> int:
        return self.response.bookingid

@pytest.fixture
def booking_client():
    client = ClientFactory.get_public_booking_client()
    yield client
    client.close()


@pytest.fixture
def valid_create_booking_request():
    return CreateBookingRequestFactory.build()

@pytest.fixture
def created_booking(
    booking_client: PublicBookingClient,
    valid_create_booking_request: CreateBookingRequestSchema
    ) -> BookingFixture:
    """
    Fixture of the created reservation.
    Returns a validated BookingFixture container.
    """
    request=valid_create_booking_request
    response = booking_client.create_booking(request)
    return BookingFixture(request=request, response=response)

@pytest.fixture
def booking_private_client(auth_cookies: Cookies):
    client = ClientFactory.get_private_booking_client(auth_cookies)
    yield client
    client.close()


@pytest.fixture
def booking_private_client_invalid(invalid_cookies: Cookies):
    """PrivateBookingClient с невалидными cookies."""
    client = ClientFactory.get_private_booking_client(invalid_cookies)
    yield client
    client.close()