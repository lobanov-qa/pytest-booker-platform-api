from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.booking.public_booking_client import PublicBookingClient
from clients.booking.booking_schema import (
    CreateBookingRequestSchema,
    CreateBookingResponseSchema,
    UnavailableDatesResponseSchema,
    GetSummaryResponseSchema,
)
from clients.booking.routes import BookingRoutes
from clients.errors_schema import ValidationErrorSchema, BaseErrorResponse
from data_factories.booking_factory import CreateBookingRequestFactory
from data_factories.query_factories import (
    UnavailableDatesQueryFactory,
    GetSummaryQueryFactory,
)
from fixtures.booking import BookingFixture
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import (
    assert_status_code,
    assert_positive,
    assert_is_instance,
    assert_in,
    assert_length_equal,
)
from utils.assertions.booking import assert_create_booking_response
from utils.assertions.errors import assert_validation_error, assert_base_error_response
from utils.assertions.schema import validate_json_schema


@pytest.mark.booking
@pytest.mark.regression
@allure.tag(AllureTag.BOOKING)
@allure.epic(AllureEpic.BOOKING)
@allure.feature(AllureFeature.BOOKING_CRUD)
class TestPublicBookingAPI:
    """
    Test suite for public booking operations (no authentication required).
    Covers create, check availability, and summary endpoints.
    """

    @pytest.mark.smoke
    @allure.story(AllureStory.BOOKING_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("POST /booking - Create booking successfully (201)")
    @allure.severity(Severity.BLOCKER)
    def test_create_booking_201(
        self,
        booking_client: PublicBookingClient,
        valid_create_booking_request: CreateBookingRequestSchema,
    ):
        """
        Positive test: Create booking with full validation.
        Validates response structure and JSON schema compliance.
        """
        response = booking_client.create_booking_api(valid_create_booking_request)
        assert_status_code(response.status_code, HTTPStatus.CREATED)
        response_data = CreateBookingResponseSchema.model_validate_json(response.text)
        assert_create_booking_response(valid_create_booking_request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.BOOKING_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("POST /booking - High-level method for creating booking")
    @allure.severity(Severity.NORMAL)
    def test_create_booking_high_level(
        self,
        booking_client: PublicBookingClient,
        valid_create_booking_request: CreateBookingRequestSchema,
    ):
        """
        Positive test: Use convenience method create_booking().
        Returns parsed Pydantic model CreateBookingResponseSchema.
        """
        response_data = booking_client.create_booking(valid_create_booking_request)
        assert_is_instance(response_data, CreateBookingResponseSchema, "response_data")
        assert_positive(response_data.bookingid, "bookingid")
        assert_create_booking_response(valid_create_booking_request, response_data)

    @allure.story(AllureStory.BOOKING_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("POST /booking - Create booking with roomid=0 (400)")
    @allure.severity(Severity.NORMAL)
    def test_create_booking_invalid_roomid_zero(self, booking_client: PublicBookingClient):
        """
        Negative test: Create booking with roomid=0 (must be >=1).
        Should return 400 Bad Request with validation error.
        """
        request = CreateBookingRequestFactory.build()
        request.roomid = 0

        response = booking_client.create_booking_api(request)
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        error_data = ValidationErrorSchema.model_validate_json(response.text)
        assert_validation_error(error_data, expected_fields=["greater", "equal"])

    @allure.story(AllureStory.BOOKING_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("POST /booking - Create booking with short firstname (400)")
    @allure.severity(Severity.NORMAL)
    def test_create_booking_short_firstname(self, booking_client: PublicBookingClient):
        """
        Negative test: Create booking with firstname less than 3 characters.
        Should return 400 Bad Request with validation error.
        """
        request = CreateBookingRequestFactory.build()
        request.firstname = "Ab"

        response = booking_client.create_booking_api(request)
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        error_data = ValidationErrorSchema.model_validate_json(response.text)
        assert_validation_error(error_data, expected_fields=["between"])

    @allure.story(AllureStory.BOOKING_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("POST /booking - Create booking without firstname field (400)")
    @allure.severity(Severity.NORMAL)
    def test_create_booking_missing_firstname(self, booking_client: PublicBookingClient):
        """
        Negative test: Create booking without required firstname field.
        Should return 400 Bad Request with validation error.
        """
        data = CreateBookingRequestFactory.build().model_dump(mode="json")
        del data["firstname"]

        response = booking_client.post(BookingRoutes.ROOT, json=data)
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        error_data = ValidationErrorSchema.model_validate_json(response.text)
        assert_validation_error(error_data, expected_fields=["firstname"])

    @allure.story(AllureStory.AVAILABILITY_CHECK)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /booking/unavailable - Check availability for free date range")
    @allure.severity(Severity.NORMAL)
    def test_unavailable_dates_free_range(self, booking_client: PublicBookingClient):
        """
        Positive test: Check availability for free date range.
        Should return empty list or list without conflicts.
        """
        query = UnavailableDatesQueryFactory.build()
        response = booking_client.get_unavailable_api(query)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = UnavailableDatesResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_is_instance(response_data.root, list, "response_data.root")

    @pytest.mark.smoke
    @allure.story(AllureStory.AVAILABILITY_CHECK)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.severity(Severity.CRITICAL)
    def test_unavailable_dates_booked_period(
        self,
        created_booking: BookingFixture,
        booking_client: PublicBookingClient,
    ):
        """
        Positive test: Check availability during already booked period.
        Should return the room as unavailable.
        """
        dates = created_booking.response.booking.bookingdates
        allure.dynamic.title(
            f"GET /booking/unavailable - Check availability during booked period "
            f"({dates.checkin} - {dates.checkout})"
        )
        query = UnavailableDatesQueryFactory.build(
            checkin=dates.checkin.isoformat(),
            checkout=dates.checkout.isoformat(),
        )
        response = booking_client.get_unavailable_api(query)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = UnavailableDatesResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_is_instance(response_data.root, list, "response_data.root")

        booked_roomid = created_booking.request.roomid
        unavailable_roomids = {room.roomid for room in response_data.root}
        assert_in(booked_roomid, list(unavailable_roomids), "unavailable_roomids")

    @allure.story(AllureStory.AVAILABILITY_CHECK)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /booking/unavailable - High-level method for checking availability")
    @allure.severity(Severity.NORMAL)
    def test_unavailable_dates_high_level(self, booking_client: PublicBookingClient):
        """
        Positive test: Use convenience method get_unavailable_rooms().
        Returns parsed Pydantic model UnavailableDatesResponseSchema.
        """
        query = UnavailableDatesQueryFactory.build()
        response_data = booking_client.get_unavailable_rooms(query)
        assert_is_instance(response_data, UnavailableDatesResponseSchema, "response_data")
        assert_is_instance(response_data.root, list, "response_data.root")
        for room in response_data.root:
            assert_positive(room.roomid, "roomid")

    @allure.story(AllureStory.AVAILABILITY_CHECK)
    @allure.tag(AllureTag.GET_ENTITIES, AllureTag.NEGATIVE)
    @allure.title("GET /booking/unavailable - Missing checkin/checkout parameter (400)")
    @pytest.mark.parametrize("missing_param", ["checkin", "checkout"])
    @allure.severity(Severity.NORMAL)
    def test_unavailable_dates_missing_param(
        self,
        booking_client: PublicBookingClient,
        missing_param: str,
    ):
        """
        Negative test: Check availability with missing required parameter.
        Should return 400 Bad Request.
        """
        params = {"checkin": "2025-01-01", "checkout": "2025-01-10"}
        del params[missing_param]
        response = booking_client.get(BookingRoutes.UNAVAILABLE, params=params)
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        error_data = BaseErrorResponse.model_validate_json(response.text)
        assert_base_error_response(error_data, path_contains="unavailable")

    @allure.story(AllureStory.AVAILABILITY_CHECK)
    @allure.tag(AllureTag.GET_ENTITIES, AllureTag.NEGATIVE)
    @allure.title("GET /booking/unavailable - Non-existent date (500)")
    @allure.severity(Severity.MINOR)
    def test_unavailable_dates_nonexistent_date_500(self, booking_client: PublicBookingClient):
        """
        Negative test: Check availability with non-existent date.
        API returns 500 INTERNAL_SERVER_ERROR.
        """
        params = {"checkin": "2026-01-40", "checkout": "2026-01-45"}
        response = booking_client.get(BookingRoutes.UNAVAILABLE, params=params)
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        error_data = BaseErrorResponse.model_validate_json(response.text)
        assert_base_error_response(error_data, expected_status=500, path_contains="unavailable")

    @allure.story(AllureStory.AVAILABILITY_CHECK)
    @allure.tag(AllureTag.GET_ENTITIES, AllureTag.NEGATIVE)
    @allure.title("GET /booking/unavailable - Invalid date format (500)")
    @allure.severity(Severity.MINOR)
    def test_unavailable_dates_invalid_format_500(self, booking_client: PublicBookingClient):
        """
        Negative test: Check availability with invalid date format.
        API returns 500 INTERNAL_SERVER_ERROR.
        """
        params = {"checkin": "2026-01-20", "checkout": "2026/01/30"}
        response = booking_client.get(BookingRoutes.UNAVAILABLE, params=params)
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        error_data = BaseErrorResponse.model_validate_json(response.text)
        assert_base_error_response(error_data, expected_status=500, path_contains="unavailable")

    @allure.story(AllureStory.BOOKING_SUMMARY)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /booking/summary - Get booking summary for valid room ID")
    @allure.severity(Severity.NORMAL)
    def test_get_summary_valid_roomid(
        self,
        created_booking: BookingFixture,
        booking_client: PublicBookingClient,
    ):
        """
        Positive test: Get booking summary for existing room ID.
        Validates response structure and JSON schema.
        """
        roomid = created_booking.response.booking.roomid
        query = GetSummaryQueryFactory.build(roomid=roomid)
        response = booking_client.get_summary_api(query)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = GetSummaryResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_is_instance(response_data.bookings, list, "bookings")

    @allure.story(AllureStory.BOOKING_SUMMARY)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("roomid", ["0", "-1", "-999"])
    def test_get_summary_with_non_positive_roomid_returns_empty_list(
        self,
        booking_client: PublicBookingClient,
        roomid: str,
    ):
        """
        Positive test: Get summary with non-positive roomid.
        API returns 200 OK with empty bookings list.
        """
        allure.dynamic.title(f"GET /booking/summary?roomid={roomid} - Non-positive roomid returns empty list")
        params = {"roomid": roomid}
        response = booking_client.get(BookingRoutes.SUMMARY, params=params)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = GetSummaryResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_is_instance(response_data.bookings, list, "bookings")
        assert_length_equal(response_data.bookings, 0, "bookings")

    @allure.story(AllureStory.BOOKING_SUMMARY)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /booking/summary - High-level method for getting summary")
    @allure.severity(Severity.NORMAL)
    def test_get_summary_high_level(self, booking_client: PublicBookingClient):
        """
        Positive test: Use convenience method get_booking_summary().
        Returns parsed Pydantic model GetSummaryResponseSchema.
        """
        query = GetSummaryQueryFactory.build()
        response_data = booking_client.get_booking_summary(query)
        assert_is_instance(response_data, GetSummaryResponseSchema, "response_data")
        assert_is_instance(response_data.bookings, list, "bookings")

    @allure.story(AllureStory.BOOKING_SUMMARY)
    @allure.tag(AllureTag.GET_ENTITIES, AllureTag.NEGATIVE)
    @allure.title("GET /booking/summary - Missing roomid parameter (400)")
    @allure.severity(Severity.NORMAL)
    def test_get_summary_missing_roomid(self, booking_client: PublicBookingClient):
        """
        Negative test: Get summary without required roomid parameter.
        Should return 400 Bad Request.
        """
        response = booking_client.get(BookingRoutes.SUMMARY, params={})
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        error_data = BaseErrorResponse.model_validate_json(response.text)
        assert_base_error_response(error_data, expected_status=400, path_contains="summary")

    @allure.story(AllureStory.BOOKING_SUMMARY)
    @allure.tag(AllureTag.GET_ENTITIES, AllureTag.NEGATIVE)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("invalid_value", ["", "one", "abc123"])
    def test_get_summary_invalid_roomid_non_number(
        self,
        booking_client: PublicBookingClient,
        invalid_value: str,
    ):
        """
        Negative test: Get summary with non-numeric roomid.
        API returns 500 INTERNAL_SERVER_ERROR.
        """
        allure.dynamic.title(f"GET /booking/summary?roomid={invalid_value} - Non-numeric roomid (500)")
        params = {"roomid": invalid_value}
        response = booking_client.get(BookingRoutes.SUMMARY, params=params)
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        error_data = BaseErrorResponse.model_validate_json(response.text)
        assert_base_error_response(error_data, expected_status=500, path_contains="summary")
