import pytest

from pydantic import BaseModel
from httpx import Cookies

from clients.message.message_schema import CreateMessageRequestSchema, MessageSchema
from clients.message.public_message_client import PublicMessageClient
from clients.client_factories import ClientFactory
from data_factories.message_factory import MessageRequestFactory


class MessageFixture(BaseModel):
    """
    Message context - used to pass data between tests and validation.
    """
    request: CreateMessageRequestSchema
    response: MessageSchema

    @property
    def message_id(self) -> int:
        return self.response.messageid


@pytest.fixture
def public_message_client():
    client = ClientFactory.get_public_message_client()
    yield client
    client.close()


@pytest.fixture
def private_message_client(auth_cookies: Cookies):
    client = ClientFactory.get_private_message_client(auth_cookies)
    yield client
    client.close()


@pytest.fixture
def private_message_client_invalid(invalid_cookies: Cookies):
    """PrivateMessageClient with invalid cookies for negative auth tests."""
    client = ClientFactory.get_private_message_client(invalid_cookies)
    yield client
    client.close()


@pytest.fixture
def valid_message_request():
    return MessageRequestFactory.build()


@pytest.fixture
def created_message(
    public_message_client: PublicMessageClient,
    valid_message_request: CreateMessageRequestSchema,
) -> MessageFixture:
    """
    Fixture of the created message.
    Returns a validated MessageFixture container.
    """
    request = valid_message_request
    response = public_message_client.create_message(request)
    return MessageFixture(request=request, response=response)
