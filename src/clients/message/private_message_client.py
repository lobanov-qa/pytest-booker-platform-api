import allure
from httpx import Response, Cookies

from clients.api_client import APIClient
from clients.message.message_schema import MessageSchema
from clients.message.routes import MessageRoutes
from clients.api_coverage import tracker_message


class PrivateMessageClient(APIClient):
    """
    Private client for the message API.

    Supports raw responses (_api methods) for full control in negative tests,
    and high-level parsed methods (returning Pydantic models) for positive flows.
    Designed to be used with authenticated session cookies.
    """

    def __init__(self, base_url: str, timeout: float, cookies: Cookies, event_hooks=None, **kwargs):
        """
        :param base_url: Base URL of the message service (e.g., http://localhost:3006).
        :param timeout: Request timeout in seconds.
        :param cookies: Session cookies obtained via authentication (e.g., from AuthClient.login).
        :param event_hooks: Optional hooks for logging, cURL printing, etc.
        :param kwargs: Additional arguments passed to APIClient.
        """
        super().__init__(base_url=base_url, timeout=timeout, cookies=cookies, event_hooks=event_hooks, **kwargs)

    @allure.step("Get message by ID {messageid}")
    @tracker_message.track_coverage_httpx(MessageRoutes.MESSAGE_ID)
    def get_message_api(self, messageid: int) -> Response:
        """
        Retrieve a message by ID (raw response).
        :param messageid: ID of the message.
        :return: Raw HTTP response.
        """
        path = MessageRoutes.MESSAGE_ID.format(id=messageid)
        return self.get(path)

    def get_message(self, messageid: int) -> MessageSchema:
        """
        High-level method: get message by ID (success path).
        :param messageid: ID of the message.
        :return: Parsed response model.
        :raises HTTPStatusError: If status != 2xx.
        """
        response = self.get_message_api(messageid)
        return self.parse_response(response, MessageSchema)

    @allure.step("Mark message as read #{messageid}")
    @tracker_message.track_coverage_httpx(MessageRoutes.MESSAGE_READ)
    def mark_read_api(self, messageid: int) -> Response:
        """
        Mark a message as read (raw response).
        :param messageid: ID of the message.
        :return: Raw HTTP response.
        """
        path = MessageRoutes.MESSAGE_READ.format(id=messageid)
        return self.put(path)

    def mark_read(self, messageid: int) -> None:
        """
        High-level method: mark message as read by ID (success path).
        :param messageid: ID of the message.
        :raises HTTPStatusError: If status != 2xx.
        """
        response = self.mark_read_api(messageid)
        response.raise_for_status()

    @allure.step("Delete message #{messageid}")
    @tracker_message.track_coverage_httpx(MessageRoutes.MESSAGE_ID)
    def delete_message_api(self, messageid: int) -> Response:
        """
        Delete a message by ID (raw response).
        :param messageid: ID of the message to delete.
        :return: Raw HTTP response.
        """
        path = MessageRoutes.MESSAGE_ID.format(id=messageid)
        return self.delete(path)

    def delete_message(self, messageid: int) -> None:
        """
        High-level method: delete message by ID (success path).
        :param messageid: ID of the message.
        :raises HTTPStatusError: If status != 2xx.
        """
        response = self.delete_message_api(messageid)
        response.raise_for_status()