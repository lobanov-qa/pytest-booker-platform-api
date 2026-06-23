import allure
from httpx import Response, Cookies

from clients.api_client import APIClient
from clients.report.report_schema import ReportSchema
from clients.report.routes import ReportRoutes
from clients.api_coverage import tracker_report


class PrivateReportClient(APIClient):
    """
    Private client for the report API.

    Supports raw responses (_api methods) for negative tests
    and parsed models (domain methods) for positive flows.
    Designed to be used with authenticated session cookies.
    """

    def __init__(self, base_url: str, timeout: float, cookies: Cookies, event_hooks=None, **kwargs):
        """
        :param base_url: Base URL of the report service (e.g., http://localhost:3005).
        :param timeout: Request timeout in seconds.
        :param cookies: Session cookies obtained via authentication (e.g., from AuthClient.login).
        :param event_hooks: Optional hooks for logging, cURL printing, etc.
        :param kwargs: Additional arguments passed to APIClient.
        """
        super().__init__(base_url=base_url, timeout=timeout, cookies=cookies, event_hooks=event_hooks, **kwargs)

    @allure.step("Get all room reports")
    @tracker_report.track_coverage_httpx(ReportRoutes.ROOT)
    def get_all_reports_api(self) -> Response:
        """
        Retrieve all room reports (raw response).
        :return: HTTP response.
        """
        return self.get(ReportRoutes.ROOT)

    def get_all_reports(self) -> ReportSchema:
        """
        High-level method: get all reports and return parsed model (expects success).
        :return: Parsed response model.
        :raises HTTPStatusError: If status != 2xx.
        """
        response = self.get_all_reports_api()
        return self.parse_response(response, ReportSchema)