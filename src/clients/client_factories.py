from clients.auth.auth_client import AuthClient
from clients.booking.private_booking_client import PrivateBookingClient
from clients.booking.public_booking_client import PublicBookingClient
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from clients.room.public_room_client import PublicRoomClient
from config import settings


class ClientFactory:
    """
    Factory class for creating configured API clients.

    This factory centralizes the instantiation of clients with proper configuration
    (base URL, timeout) pulled from settings, ensuring consistency across tests.
    It does not perform HTTP requests itself — only constructs and returns client instances.
    """
    @staticmethod
    def get_auth_client() -> AuthClient:
        """
        Creates and returns a configured AuthClient instance.

        :return: AuthClient configured with base URL and timeout from settings.
        :rtype: AuthClient
        """
        return AuthClient(
            base_url=settings.auth.client_url,
            timeout=settings.http_client.timeout,
            event_hooks={
                "request": [curl_event_hook, log_request_event_hook],
                "response": [log_response_event_hook]
                }
        )

    @staticmethod
    def get_public_booking_client() -> PublicBookingClient:
        """
        Creates and returns a configured PublicBookingClient instance.

        :return: PublicBookingClient configured with base URL and timeout from settings.
        :rtype: PublicBookingClient
        """
        return PublicBookingClient(
            base_url=settings.booking.client_url,
            timeout=settings.http_client.timeout,
            event_hooks={
                "request": [curl_event_hook, log_request_event_hook],
                "response": [log_response_event_hook]
            }
        )

    @staticmethod
    def get_private_booking_client(cookies) -> PrivateBookingClient:
        """
        Creates and returns a configured PrivateBookingClient instance.

        :return: PrivateBookingClient configured with base URL,timeout and cookies from settings.
        :rtype: PrivateBookingClient
        """
        return PrivateBookingClient(
            base_url=settings.booking.client_url,
            timeout=settings.http_client.timeout,
            cookies=cookies,
            event_hooks={
                "request": [curl_event_hook, log_request_event_hook],
                "response": [log_response_event_hook]
            }
        )

    @staticmethod
    def get_public_room_client() -> PublicRoomClient:
        """
        Creates and returns a configured PublicRoomClient instance.

        :return: PublicRoomClient configured with base URL and timeout from settings.
        :rtype: PublicRoomClient
        """
        return PublicRoomClient(
            base_url=settings.room.client_url,
            timeout=settings.http_client.timeout,
            event_hooks={
                "request": [curl_event_hook, log_request_event_hook],
                "response": [log_response_event_hook]
            }
        )