import pytest

from pydantic import BaseModel
from httpx import Cookies

from clients.room.room_schema import RoomRequestSchema, RoomResponseSchema
from clients.room.private_room_client import PrivateRoomClient
from clients.client_factories import ClientFactory
from data_factories.room_factory import RoomRequestFactory


class RoomFixture(BaseModel):
    """
    Room context - used to pass data between tests and validation.
    """
    request: RoomRequestSchema
    response: RoomResponseSchema

    @property
    def room_id(self) -> int:
        return self.response.roomid


@pytest.fixture
def public_room_client():
    client = ClientFactory.get_public_room_client()
    yield client
    client.close()


@pytest.fixture
def private_room_client(auth_cookies: Cookies):
    client = ClientFactory.get_private_room_client(auth_cookies)
    yield client
    client.close()


@pytest.fixture
def private_room_client_invalid(invalid_cookies: Cookies):
    """PrivateRoomClient with invalid cookies for negative auth tests."""
    client = ClientFactory.get_private_room_client(invalid_cookies)
    yield client
    client.close()


@pytest.fixture
def valid_room_request():
    return RoomRequestFactory.build()


@pytest.fixture
def created_room(
    private_room_client: PrivateRoomClient,
    valid_room_request: RoomRequestSchema,
) -> RoomFixture:
    """
    Fixture of the created room.
    Returns a validated RoomFixture container.
    """
    request = valid_room_request
    response = private_room_client.create_room(request)
    return RoomFixture(request=request, response=response)