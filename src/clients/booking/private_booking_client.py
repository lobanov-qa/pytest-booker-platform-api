from typing import Optional
import allure
from httpx import Response, Cookies

from clients.api_client import APIClient
from clients.booking.booking_schema import (
    GetBookingQuerySchema,
    GetBookingsResponseSchema,
    UpdateBookingRequestSchema,
    UpdateBookingResponseSchema,
    BookingSchema
)
from clients.booking.routes import BookingRoutes
from clients.api_coverage import tracker_booking


class PrivateBookingClient(APIClient):
    """
    Private client for the booking API.

    Supports raw responses (_api methods) for full control in negative tests,
    and high-level parsed methods (returning Pydantic models) for positive flows.
    Designed to be used with authenticated session cookies.
    """

    def __init__(self, base_url: str, timeout: float, cookies: Cookies, event_hooks=None, **kwargs):
        """
        :param base_url: Base URL of the booking service (e.g., http://localhost:3000).
        :param timeout: Request timeout in seconds.
        :param cookies: Session cookies obtained via authentication (e.g., from AuthClient.login).
        :param event_hooks: Optional hooks for logging, cURL printing, etc.
        :param kwargs: Additional arguments passed to APIClient.
        """
        super().__init__(base_url=base_url, timeout=timeout, cookies=cookies, event_hooks=event_hooks, **kwargs)

    @allure.step("Get all bookings")
    @tracker_booking.track_coverage_httpx(BookingRoutes.ROOT)
    def get_bookings_api(self, query: Optional[GetBookingQuerySchema] = None) -> Response:
        """
        Retrieve all bookings with optional filtering by roomid.
        :param query: Optional query parameters (roomid).
        :return: Raw HTTP response.
        """
        params = query.model_dump(exclude_none=True) if query else None
        return self.get(BookingRoutes.ROOT, params=params)

    def get_all_bookings(self) -> GetBookingsResponseSchema:
        """
        High-level method: get all bookings (success path).
        :return: Parsed response model.
        """
        response = self.get_bookings_api()
        return self.parse_response(response, GetBookingsResponseSchema)

    def get_bookings_by_room(self, roomid: str) -> GetBookingsResponseSchema:
        """
        High-level method: get bookings filtered by roomid.
        :param roomid: ID of the room to filter by.
        :return: Parsed response model.
        """
        query = GetBookingQuerySchema(roomid=roomid)
        response = self.get_bookings_api(query)
        return self.parse_response(response, GetBookingsResponseSchema)

    @allure.step("Get booking by id {bookingid}")
    @tracker_booking.track_coverage_httpx(BookingRoutes.BOOKING_ID) 
    def get_booking_api(self, bookingid: int) -> Response:
        """
        Retrieve booking details by ID.
        :param bookingid: ID of the booking.
        :return: Raw HTTP response.
        """
        path = BookingRoutes.BOOKING_ID.format(id=bookingid)
        return self.get(path)

    def get_booking(self, bookingid: int) -> BookingSchema:
        """
        High-level method: get booking by ID (success path).
        :param bookingid: ID of the booking.
        :return: Parsed response model.
        """
        response = self.get_booking_api(bookingid)
        return self.parse_response(response, BookingSchema)

    @allure.step("Update booking by id {bookingid}")
    @tracker_booking.track_coverage_httpx(BookingRoutes.BOOKING_ID) 
    def update_booking_api(self, bookingid: int, request: UpdateBookingRequestSchema) -> Response:
        """
        Update an existing booking.
        :param bookingid: ID of the booking to update.
        :param request: Data for update (all fields optional).
        :return: Raw HTTP response.
        """
        path = BookingRoutes.BOOKING_ID.format(id=bookingid)
        return self.put(path, json=request.model_dump(mode="json"))

    def update_booking(self, bookingid: int, request: UpdateBookingRequestSchema) -> UpdateBookingResponseSchema:
        """
        High-level method: update booking (success path).
        :param bookingid: ID of the booking.
        :param request: Update data.
        :return: Parsed response model.
        """
        response = self.update_booking_api(bookingid, request)
        return self.parse_response(response, UpdateBookingResponseSchema)

    @allure.step("Delete booking by id {bookingid}")
    @tracker_booking.track_coverage_httpx(BookingRoutes.BOOKING_ID) 
    def delete_booking_api(self, bookingid: int) -> Response:
        """
        Delete a booking by ID.
        :param bookingid: ID of the booking to delete.
        :return: Raw HTTP response.
        """
        path = BookingRoutes.BOOKING_ID.format(id=bookingid)
        return self.delete(path)

    def delete_booking(self, bookingid: int) -> None:
        """
        High-level method: delete booking by ID (success path).
        :param bookingid: ID of the booking.
        """
        response = self.delete_booking_api(bookingid)
        response.raise_for_status()
