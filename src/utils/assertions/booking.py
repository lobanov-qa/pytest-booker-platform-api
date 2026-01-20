import allure

from clients.booking.booking_schema import CreateBookingRequestSchema, CreateBookingResponseSchema, BookingDates, \
    GetBookingsResponseSchema, UpdateBookingRequestSchema, UpdateBookingResponseSchema, BookingSchema
from clients.errors_schema import BaseErrorResponse
from utils.assertions.base import assert_equal, assert_is_instance, assert_positive, assert_length_equal
from utils.assertions.errors import assert_base_error_response
from utils.logger import get_logger

logger = get_logger("BOOKING_ASSERTIONS")


@allure.step("Check create booking response")
def assert_create_booking_response(request: CreateBookingRequestSchema, response: CreateBookingResponseSchema):
    """
    Verifies that the job creation response matches the request.

    :param request: Initial request to create a task.
    :param response: API response with file data.
    :raises AssertionError: If at least one field does not match.
    """
    logger.info("Check create booking response")
    assert_positive(response.booking.bookingid, "booking.bookingid not positive")
    assert_equal(response.booking.bookingid, response.bookingid, "booking.bookingid")
    assert_equal(response.booking.depositpaid, request.depositpaid, "depositpaid")
    assert_equal(response.booking.roomid, request.roomid, "roomid")
    assert_equal(response.booking.firstname, request.firstname, "firstname")
    assert_equal(response.booking.lastname, request.lastname, "lastname")
    assert_equal(response.booking.bookingdates, request.bookingdates, "bookingdates")
    

@allure.step("Assert booking dates equal")
def assert_booking_dates_equal(
    actual: BookingDates,
    expected: BookingDates
) -> None:
    """Helper method for comparing dates."""
    logger.info("Assert booking dates equal")
    assert_equal(actual.checkin, expected.checkin, "bookingdates.checkin")
    assert_equal(actual.checkout, expected.checkout, "bookingdates.checkout")


@allure.step("Check booking")
def assert_booking(actual: BookingSchema, expected: BookingSchema):
    """
    Checks that the actual booking data matches the expected one.

    :param actual: Actual booking data.
    :param expected: Expected booking data.
    :raises AssertionError: If at least one field does not match.
    """
    logger.info("Check booking")
    assert_equal(actual.bookingid, expected.bookingid, "bookingid")
    assert_equal(actual.depositpaid, expected.depositpaid, "depositpaid")
    assert_equal(actual.roomid, expected.roomid, "roomid")
    assert_equal(actual.firstname, expected.firstname, "firstname")
    assert_equal(actual.lastname, expected.lastname, "lastname")
    assert_equal(actual.bookingdates, expected.bookingdates, "bookingdates")

@allure.step("Check get booking response")
def assert_get_booking_response(
    get_response: BookingSchema,
    create_response: BookingSchema
):
    """
    Checks that the response when receiving a booking matches the response when creating it.

    :param get_response: API response when requesting booking data.
    :param create_response: Booking data from creation response.
    :raises AssertionError: If booking data does not match.
    """
    logger.info("Check get booking response")
    assert_booking(get_response, create_response)


@allure.step("Check update booking response")
def assert_update_booking_response(request: UpdateBookingRequestSchema, response: UpdateBookingResponseSchema):
    """Checking response to booking update"""
    logger.info("Check update booking response")
    assert_equal(response.bookingid, request.bookingid, "bookingid")
    assert_equal(response.booking.depositpaid, request.depositpaid, "depositpaid")
    assert_equal(response.booking.roomid, request.roomid, "roomid")
    assert_equal(response.booking.firstname, request.firstname, "firstname")
    assert_equal(response.booking.lastname, request.lastname, "lastname")
    assert_equal(response.booking.bookingdates, request.bookingdates, "bookingdates")


@allure.step("Check get bookings response")
def assert_get_bookings_response(
    get_bookings_response: GetBookingsResponseSchema,
    expected_bookings: list[BookingSchema]
):
    """
    Checks that the response when receiving a list of bookings matches the expected bookings.

    :param get_bookings_response: API response when requesting a list of bookings.
    :param expected_bookings: List of expected booking data.
    :raises AssertionError: If booking data does not match.
    """
    logger.info("Check get bookings response")
    
    actual_bookings = get_bookings_response.bookings
    assert_is_instance(actual_bookings, list, "bookings")

    for expected_booking in expected_bookings:
        found_booking = None
        for actual_booking in actual_bookings:
            if actual_booking.bookingid == expected_booking.bookingid:
                found_booking = actual_booking
                break

        assert found_booking is not None, (
            f"Expected booking with id {expected_booking.bookingid} not found in response. "
            f"Found booking ids: {[b.bookingid for b in actual_bookings]}"
        )

        assert_booking(found_booking, expected_booking)


@allure.step("Check booking not found response")
def assert_booking_not_found_response(error: BaseErrorResponse):
    """
    Function to check the error if the booking is not found on the server.

    :param error: Actual API error response.
    :raises AssertionError: If the actual response does not match the "Not Found" error.
    """
    logger.info("Check booking not found response")
    assert_base_error_response(error, expected_status=404)


