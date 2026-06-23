import allure

from httpx import Response

from clients.api_client import APIClient
from clients.report.report_schema import ReportSchema
from clients.report.routes import ReportRoutes
from clients.api_coverage import tracker_report


class PublicReportClient(APIClient):
    """
    Client for public /report/ API.

    Supports both raw responses (_api methods) for negative tests
    and parsed models (domain methods) for positive flows.
    """

    def __init__(self, base_url: str, timeout: float, event_hooks=None, **kwargs):
        super().__init__(base_url=base_url, timeout=timeout, event_hooks=event_hooks, **kwargs)

    @allure.step("Get specific room report by id {room_id}")
    @tracker_report.track_coverage_httpx(ReportRoutes.ROOM_REPORT)
    def get_room_report_api(self, room_id: int) -> Response:
        """
        Retrieve report for a specific room (raw response).
        :param room_id: ID of the room.
        :return: HTTP response.
        """
        path = ReportRoutes.ROOM_REPORT.format(id=room_id)
        return self.get(path)

    def get_room_report(self, room_id: int) -> ReportSchema:
        """
        High-level method: get room report and return parsed model (expects success).
        :param room_id: ID of the room.
        :return: Parsed response model.
        :raises HTTPStatusError: If status != 2xx.
        """
        response = self.get_room_report_api(room_id)
        return self.parse_response(response, ReportSchema)
