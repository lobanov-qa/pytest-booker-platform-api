import allure
from httpx import Response

from clients.api_client import APIClient
from clients.branding.branding_schema import BrandingSchema
from clients.branding.routes import BrandingRoutes
from clients.api_coverage import tracker_branding


class PublicBrandingClient(APIClient):
    """
    Client for public /branding/ API.

    Supports both raw responses (_api methods) for negative tests
    and parsed models (domain methods) for positive flows.
    """

    def __init__(self, base_url: str, timeout: float, event_hooks=None, **kwargs):
        """
        :param base_url: Branding service base URL.
        :param timeout: Request timeout in seconds.
        :param event_hooks: Optional hooks (logging, etc.).
        :param kwargs: Passed to APIClient.
        """
        super().__init__(base_url=base_url, timeout=timeout, event_hooks=event_hooks, **kwargs)

    @allure.step("Get branding")
    @tracker_branding.track_coverage_httpx(BrandingRoutes.ROOT)
    def get_branding_api(self) -> Response:
        """
        Get branding information (raw response).
        :return: HTTP response.
        """
        return self.get(BrandingRoutes.ROOT)

    def get_branding(self) -> BrandingSchema:
        """
        Get branding information and return parsed model (expects success).
        :return: Parsed branding model.
        :raises HTTPStatusError: If status != 2xx.
        """
        response = self.get_branding_api()
        return self.parse_response(response, BrandingSchema)
