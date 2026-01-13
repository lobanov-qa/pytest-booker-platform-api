import allure

from clients.booking.booking_schema import CreateBookingRequestSchema, CreateBookingResponseSchema,  BookingDates
from utils.assertions.base import assert_equal
from utils.logger import get_logger

logger = get_logger("BOOKING_ASSERTIONS")


@allure.step("Check create booking response")
def assert_create_booking_response(request: CreateBookingRequestSchema, response: CreateBookingResponseSchema):
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create booking response")
    assert response.bookingid > 0, f"bookingid должен быть положительным, получили {response.bookingid}"
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
    """Вспомогательный метод для сравнения дат."""
    logger.info("Assert booking dates equal")
    assert_equal(actual.checkin, expected.checkin, "bookingdates.checkin")
    assert_equal(actual.checkout, expected.checkout, "bookingdates.checkout")