from httpx import Cookies

from clients.auth.auth_client import AuthClient
from clients.booking.private_booking_client import PrivateBookingClient
from clients.booking.public_booking_client import PublicBookingClient
from clients.branding.private_branding_client import PrivateBrandingClient
from clients.branding.public_branding_client import PublicBrandingClient
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from clients.message.private_message_client import PrivateMessageClient
from clients.message.public_message_client import PublicMessageClient
from clients.report.private_report_client import PrivateReportClient
from clients.report.public_report_client import PublicReportClient
from clients.room.public_room_client import PublicRoomClient
from clients.room.private_room_client import PrivateRoomClient
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

    @staticmethod
    def get_private_room_client(cookies: Cookies) -> PrivateRoomClient:
        """
        Creates and returns a configured PrivateRoomClient instance.
        :param cookies: Auth cookies obtained via authentication.
        :return: PrivateRoomClient configured with base URL, timeout and cookies.
        """
        return PrivateRoomClient(
            base_url=settings.room.client_url,
            timeout=settings.http_client.timeout,
            cookies=cookies,
            event_hooks={
                "request": [curl_event_hook, log_request_event_hook],
                "response": [log_response_event_hook]
            }
        )

    @staticmethod
    def get_public_branding_client() -> PublicBrandingClient:
        """
        Creates and returns a configured PublicBrandingClient instance.

        :return: PublicBrandingClient configured with base URL and timeout from settings.
        :rtype: PublicBrandingClient
        """
        return PublicBrandingClient(
            base_url=settings.branding.client_url,
            timeout=settings.http_client.timeout,
            event_hooks={
                "request": [curl_event_hook, log_request_event_hook],
                "response": [log_response_event_hook]
            }
        )

    @staticmethod
    def get_private_branding_client(cookies: Cookies) -> PrivateBrandingClient:
        """
        Creates and returns a configured PrivateBrandingClient instance with auth cookies.

        :param cookies: Auth cookies obtained via authentication.
        :return: PrivateBrandingClient configured with base URL, timeout, and cookies.
        :rtype: PrivateBrandingClient
        """
        return PrivateBrandingClient(
            base_url=settings.branding.client_url,
            timeout=settings.http_client.timeout,
            cookies=cookies,
            event_hooks={
                "request": [curl_event_hook, log_request_event_hook],
                "response": [log_response_event_hook]
            }
        )

    @staticmethod
    def get_public_message_client() -> PublicMessageClient:
        """
        Creates and returns a configured PublicMessageClient instance.

        :return: PublicMessageClient configured with base URL and timeout from settings.
        :rtype: PublicMessageClient
        """
        return PublicMessageClient(
            base_url=settings.message.client_url,
            timeout=settings.http_client.timeout,
            event_hooks={
                "request": [curl_event_hook, log_request_event_hook],
                "response": [log_response_event_hook]
            }
        )

    @staticmethod
    def get_private_message_client(cookies: Cookies) -> PrivateMessageClient:
        """
        Creates and returns a configured PrivateMessageClient instance with auth cookies.

        :param cookies: Auth cookies obtained via authentication.
        :return: PrivateMessageClient configured with base URL, timeout, and cookies.
        :rtype: PrivateMessageClient
        """
        return PrivateMessageClient(
            base_url=settings.message.client_url,
            timeout=settings.http_client.timeout,
            cookies=cookies,
            event_hooks={
                "request": [curl_event_hook, log_request_event_hook],
                "response": [log_response_event_hook]
            }
        )

    @staticmethod
    def get_public_report_client() -> PublicReportClient:
        """
        Creates and returns a configured PublicReportClient instance.

        :return: PublicReportClient configured with base URL and timeout from settings.
        :rtype: PublicReportClient
        """
        return PublicReportClient(
            base_url=settings.report.client_url,
            timeout=settings.http_client.timeout,
            event_hooks={
                "request": [curl_event_hook, log_request_event_hook],
                "response": [log_response_event_hook]
            }
        )

    @staticmethod
    def get_private_report_client(cookies: Cookies) -> PrivateReportClient:
        """
        Creates and returns a configured PrivateReportClient instance with auth cookies.

        :param cookies: Auth cookies obtained via authentication.
        :return: PrivateReportClient configured with base URL, timeout, and auth cookies.
        :rtype: PrivateReportClient
        """
        return PrivateReportClient(
            base_url=settings.report.client_url,
            timeout=settings.http_client.timeout,
            cookies=cookies,
            event_hooks={
                "request": [curl_event_hook, log_request_event_hook],
                "response": [log_response_event_hook]
            }
        )