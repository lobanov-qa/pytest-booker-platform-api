from clients.auth.auth_client import AuthClient
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
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



