import allure

from httpx import Response

from clients.api_client import APIClient
from clients.message.message_schema import (
    CreateMessageRequestSchema,
    MessageSchema,
    MessagesResponseSchema,
    CountSchema,
)
from clients.message.routes import MessageRoutes
from clients.api_coverage import tracker_message


class PublicMessageClient(APIClient):
    """
    Client for message API.

    Supports both raw responses (_api methods) for negative tests
    and parsed models (domain methods) for positive flows.
    """

    def __init__(self, base_url: str, timeout: float, event_hooks=None, **kwargs):
        """
        :param base_url: Message service base URL.
        :param timeout: Request timeout in seconds.
        :param event_hooks: Optional hooks (logging, etc.).
        :param kwargs: Passed to APIClient.
        """
        super().__init__(base_url=base_url, timeout=timeout, event_hooks=event_hooks, **kwargs)

    @allure.step("Create message")
    @tracker_message.track_coverage_httpx(MessageRoutes.ROOT)
    def create_message_api(self, request: CreateMessageRequestSchema) -> Response:
        """
        Create a new message (raw response). For full control in negative tests.
        :param request: Message data.
        :return: HTTP response.
        """
        return self.post(MessageRoutes.ROOT, json=request.model_dump(mode="json"))

    def create_message(self, request: CreateMessageRequestSchema) -> MessageSchema:
        """
        Create a new message and return parsed model (expects success).
        :param request: Valid message data.
        :return: Response model with message ID.
        :raises HTTPStatusError: If status != 2xx.
        """
        return self.parse_response(self.create_message_api(request), MessageSchema)

    @allure.step("Get all messages")
    @tracker_message.track_coverage_httpx(MessageRoutes.ROOT)
    def get_messages_api(self) -> Response:
        """
        Get all messages (raw response).
        :return: HTTP response with message summaries.
        """
        return self.get(MessageRoutes.ROOT)

    def get_messages(self) -> MessagesResponseSchema:
        """
        Get all messages and return parsed model (expects success).
        :return: Parsed response with list of message summaries.
        :raises HTTPStatusError: If status != 2xx.
        """
        return self.parse_response(self.get_messages_api(), MessagesResponseSchema)

    @allure.step("Get message count")
    @tracker_message.track_coverage_httpx(MessageRoutes.COUNT)
    def get_count_api(self) -> Response:
        """
        Get total message count (raw response).
        :return: HTTP response with count.
        """
        return self.get(MessageRoutes.COUNT)

    def get_count(self) -> CountSchema:
        """
        Get total message count and return parsed model (expects success).
        :return: Parsed count model.
        :raises HTTPStatusError: If status != 2xx.
        """
        return self.parse_response(self.get_count_api(), CountSchema)