from collections.abc import Generator
from typing import Any

import pytest
from httpx import Cookies
from pydantic import BaseModel

from clients.client_factories import ClientFactory
from clients.message.message_schema import CreateMessageRequestSchema, MessageSchema
from clients.message.public_message_client import PublicMessageClient
from data_factories.message_factory import MessageRequestFactory


class MessageFixture(BaseModel):
    """Message context - used to pass data between tests and validation."""

    request: CreateMessageRequestSchema
    response: MessageSchema

    @property
    def message_id(self) -> int:
        """Returns the message ID from the fixture response."""
        return self.response.messageid


@pytest.fixture
def public_message_client() -> Generator[Any, None, None]:
    client = ClientFactory.get_public_message_client()
    yield client
    client.close()


@pytest.fixture
def private_message_client(auth_cookies: Cookies) -> Generator[Any, None, None]:
    client = ClientFactory.get_private_message_client(auth_cookies)
    yield client
    client.close()


@pytest.fixture
def private_message_client_invalid(
    invalid_cookies: Cookies,
) -> Generator[Any, None, None]:
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
