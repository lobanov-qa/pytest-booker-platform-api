import allure

from httpx import Response

from clients.api_client import APIClient
from clients.booking.booking_schema import (
    CreateBookingRequestSchema,
    CreateBookingResponseSchema,
    UnavailableDatesQuerySchema,
    UnavailableDatesResponseSchema,
    GetSummaryQuerySchema,
    GetSummaryResponseSchema,
)
from clients.booking.routes import BookingRoutes
from clients.api_coverage import tracker_booking


class PublicBookingClient(APIClient):
    """
    Client for booking API.

    Supports both raw responses (_api methods) for negative tests
    and parsed models (domain methods) for positive flows.
    """

    def __init__(self, base_url: str, timeout: float, event_hooks=None, **kwargs):
        """
        :param base_url: Booking service base URL.
        :param timeout: Request timeout in seconds.
        :param event_hooks: Optional hooks (logging, etc.).
        :param kwargs: Passed to APIClient.
        """
        super().__init__(base_url=base_url, timeout=timeout, event_hooks=event_hooks, **kwargs)

    @allure.step("Create booking")
    @tracker_booking.track_coverage_httpx(BookingRoutes.ROOT)
    def create_booking_api(self, request: CreateBookingRequestSchema) -> Response:
        """
        Create booking (raw response). For full control in negative tests.
        :param request: Booking data.
        :return: HTTP response.
        """
        return self.post(BookingRoutes.ROOT, json=request.model_dump(mode='json', exclude_none=True))

    def create_booking(self, request: CreateBookingRequestSchema) -> CreateBookingResponseSchema:
        """
        Create booking and return parsed model (expects success).
        :param request: Valid booking data.
        :return: Response model with booking ID.
        :raises HTTPStatusError: If status != 2xx.
        """
        return self.parse_response(self.create_booking_api(request), CreateBookingResponseSchema)

    @allure.step("Get unavailable dates")
    @tracker_booking.track_coverage_httpx(BookingRoutes.UNAVAILABLE)
    def get_unavailable_api(self, query: UnavailableDatesQuerySchema) -> Response:
        """
        Get unavailable rooms for date range (raw response).
        :param query: Check-in/check-out dates.
        :return: HTTP response with room IDs.
        """
        return self.get(BookingRoutes.UNAVAILABLE, params=query.model_dump())

    def get_unavailable_rooms(self, query: UnavailableDatesQuerySchema) -> UnavailableDatesResponseSchema:
        """
        Get unavailable rooms and return parsed model (expects success).
        :param query: Date range.
        :return: Parsed response with room IDs.
        :raises HTTPStatusError: If status != 2xx.
        """
        return self.parse_response(self.get_unavailable_api(query), UnavailableDatesResponseSchema)

    @allure.step("Get booking date ranges")
    @tracker_booking.track_coverage_httpx(BookingRoutes.SUMMARY)
    def get_summary_api(self, query: GetSummaryQuerySchema) -> Response:
        """
        Get booking date ranges for room (raw response).
        :param query: Room ID.
        :return: HTTP response with date ranges.
        """
        return self.get(BookingRoutes.SUMMARY, params=query.model_dump())

    def get_booking_summary(self, query: GetSummaryQuerySchema) -> GetSummaryResponseSchema:
        """
        Get booking summary and return parsed model (expects success).
        :param query: Room ID.
        :return: Parsed response with date ranges.
        :raises HTTPStatusError: If status != 2xx.
        """
        return self.parse_response(self.get_summary_api(query), GetSummaryResponseSchema)
