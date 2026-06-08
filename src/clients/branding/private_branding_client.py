import allure
from httpx import Response, Cookies

from clients.api_client import APIClient
from clients.branding.branding_schema import BrandingSchema
from clients.branding.routes import BrandingRoutes
from clients.api_coverage import tracker_branding


class PrivateBrandingClient(APIClient):
    """
    Private client for the /branding/ API.

    Supports raw responses (_api methods) for full control in negative tests,
    and high-level parsed methods (returning Pydantic models) for positive flows.
    Designed to be used with authenticated session cookies.
    """

    def __init__(self, base_url: str, timeout: float, cookies: Cookies, event_hooks=None, **kwargs):
        """
        :param base_url: Base URL of the branding service (e.g., http://localhost:3002).
        :param timeout: Request timeout in seconds.
        :param cookies: Session cookies obtained via authentication (e.g., from AuthClient.login).
        :param event_hooks: Optional hooks for logging, cURL printing, etc.
        :param kwargs: Additional arguments passed to APIClient.
        """
        super().__init__(base_url=base_url, timeout=timeout, cookies=cookies, event_hooks=event_hooks, **kwargs)

    @allure.step("Update branding")
    @tracker_branding.track_coverage_httpx(BrandingRoutes.ROOT)
    def update_branding_api(self, request: BrandingSchema) -> Response:
        """
        Update branding information (raw response).
        :param request: Branding data to update (all fields optional).
        :return: HTTP response.
        """
        return self.put(BrandingRoutes.ROOT, json=request.model_dump(mode="json", by_alias=True, exclude_none=True))

    def update_branding(self, request: BrandingSchema) -> BrandingSchema:
        """
        Update branding and return parsed model (expects 202 Accepted).
        :param request: Valid branding update data.
        :return: Parsed branding model.
        :raises HTTPStatusError: If status != 2xx.
        """
        response = self.update_branding_api(request)
        return self.parse_response(response, BrandingSchema)