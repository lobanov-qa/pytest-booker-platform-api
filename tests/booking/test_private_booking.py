from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.booking.private_booking_client import PrivateBookingClient
from clients.booking.booking_schema import (
    GetBookingsResponseSchema,
    BookingSchema,
    GetBookingQuerySchema,
    UpdateBookingResponseSchema
)
from clients.booking.routes import BookingRoutes
from clients.errors_schema import BaseErrorResponse, ValidationErrorSchema
from data_factories.booking_factory import UpdateBookingRequestFactory
from fixtures.booking import BookingFixture
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import assert_status_code, assert_is_instance, assert_equal
from utils.assertions.booking import (
    assert_booking,
    assert_get_bookings_response,
    assert_get_booking_response,
    assert_update_booking_response
)
from utils.assertions.errors import assert_base_error_response, assert_validation_error
from utils.assertions.schema import validate_json_schema


@pytest.mark.booking
@pytest.mark.positive
@allure.tag(AllureTag.BOOKING)
@allure.epic(AllureEpic.BOOKING)
@allure.feature(AllureFeature.BOOKING_CRUD)
class TestPrivateBooking:
    """
    Test suite for authenticated booking operations.
    These tests require valid authentication tokens.
    """

    @allure.story(AllureStory.BOOKING_LIST)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /booking - Retrieve all bookings successfully")
    @allure.severity(Severity.BLOCKER)
    def test_get_all_bookings_success(self, booking_private_client: PrivateBookingClient):
        """
        Positive test: Retrieve all bookings with valid authentication.
        Validates response structure and JSON schema compliance.
        """
        response = booking_private_client.get_bookings_api()
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = GetBookingsResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.BOOKING_FILTERING)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.severity(Severity.BLOCKER)
    def test_get_bookings_by_room_success(
        self,
        booking_private_client: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Positive test: Filter bookings using roomid query parameter.
        Verifies filtering functionality and that only bookings for specified room are returned.
        """
        roomid = str(created_booking.response.booking.roomid)
        allure.dynamic.title(f"GET /booking?roomid={roomid} - Filter bookings by room ID")
        query = GetBookingQuerySchema(roomid=roomid)

        response = booking_private_client.get_bookings_api(query)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = GetBookingsResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())

        assert_get_bookings_response(
            get_bookings_response=response_data,
            expected_bookings=[created_booking.response.booking]
        )

        for booking in response_data.bookings:
            assert_equal(
                booking.roomid,
                created_booking.response.booking.roomid,
                f"Room ID mismatch for booking {booking.bookingid}"
            )

    @allure.story(AllureStory.BOOKING_LIST)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /booking - High-level method for retrieving all bookings")
    @allure.severity(Severity.NORMAL)
    def test_get_all_bookings_high_level(self, booking_private_client: PrivateBookingClient):
        """
        Positive test: Use convenience method get_all_bookings().
        Returns parsed Pydantic model GetBookingsResponseSchema.
        """
        response_data = booking_private_client.get_all_bookings()
        assert_is_instance(response_data, GetBookingsResponseSchema, "response_data")
        assert_is_instance(response_data.bookings, list, "bookings")

    @allure.story(AllureStory.BOOKING_FILTERING)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.severity(Severity.NORMAL)
    def test_get_bookings_by_room_high_level(
        self,
        booking_private_client: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Positive test: Use convenience method get_bookings_by_room().
        Returns parsed Pydantic model GetBookingsResponseSchema with filtered results.
        """
        roomid = str(created_booking.response.booking.roomid)
        allure.dynamic.title(f"GET /booking?roomid={roomid} - High-level method for filtered bookings")
        response_data = booking_private_client.get_bookings_by_room(roomid)
        assert_is_instance(response_data, GetBookingsResponseSchema, "response_data")
        assert_is_instance(response_data.bookings, list, "bookings")

        assert_get_bookings_response(
            get_bookings_response=response_data,
            expected_bookings=[created_booking.response.booking]
        )

    @allure.story(AllureStory.BOOKING_LIST)
    @allure.tag(AllureTag.GET_ENTITIES, AllureTag.NEGATIVE)
    @allure.title("GET /booking - Retrieve all bookings without authentication (403)")
    @allure.severity(Severity.CRITICAL)
    def test_get_all_bookings_without_auth(
        self,
        booking_private_client_invalid: PrivateBookingClient
    ):
        """
        Negative test: Attempt to retrieve all bookings without authentication.
        Should return 403 Forbidden.
        """
        response = booking_private_client_invalid.get_bookings_api()
        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)

    @allure.story(AllureStory.BOOKING_FILTERING)
    @allure.tag(AllureTag.GET_ENTITIES, AllureTag.NEGATIVE)
    @pytest.mark.parametrize("invalid_value", ["", "one", "abc123"])
    @allure.title("GET /booking?roomid={invalid_value} - Invalid room ID format (500)")
    @allure.severity(Severity.NORMAL)
    def test_get_bookings_invalid_roomid_format(
        self,
        booking_private_client: PrivateBookingClient,
        invalid_value: str
    ):
        """
        Negative test: Filter bookings with non-numeric roomid values.
        API returns 500 INTERNAL_SERVER_ERROR for invalid room ID format.
        """
        params = {"roomid": invalid_value}
        response = booking_private_client.get(BookingRoutes.ROOT, params=params)
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        error_data = BaseErrorResponse.model_validate_json(response.text)
        assert_base_error_response(error_data, expected_status=500, path_contains="booking/")

    @allure.story(AllureStory.BOOKING_FILTERING)
    @allure.tag(AllureTag.GET_ENTITIES, AllureTag.NEGATIVE)
    @allure.title("GET /booking?roomid=9999 - Query non-existent room ID")
    @allure.severity(Severity.NORMAL)
    def test_get_bookings_nonexistent_roomid(self, booking_private_client: PrivateBookingClient):
        """
        Negative test: Filter bookings with non-existent roomid.
        Should return 200 OK with empty bookings list.
        """
        query = GetBookingQuerySchema(roomid='9999')

        response = booking_private_client.get_bookings_api(query)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = GetBookingsResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())

        assert_get_bookings_response(
            get_bookings_response=response_data,
            expected_bookings=[]
        )

    @allure.story(AllureStory.BOOKING_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_get_booking_success(
        self,
        booking_private_client: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Positive test: Retrieve specific booking by booking ID.
        Validates response matches the created booking data.
        """
        booking_id = created_booking.response.bookingid
        allure.dynamic.title(f"GET /booking/{booking_id} - Retrieve specific booking by ID")
        response = booking_private_client.get_booking_api(booking_id)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = BookingSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_get_booking_response(response_data, created_booking.response.booking)

    @allure.story(AllureStory.BOOKING_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_get_booking_high_level(
        self,
        booking_private_client: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Positive test: Use convenience method get_booking().
        Returns parsed Pydantic model BookingSchema.
        """
        booking_id = created_booking.response.bookingid
        allure.dynamic.title(f"GET /booking/{booking_id} - Retrieve specific booking by ID")
        response_data = booking_private_client.get_booking(booking_id)
        assert_is_instance(response_data, BookingSchema, "response_data")
        assert_get_booking_response(response_data, created_booking.response.booking)

    @allure.story(AllureStory.BOOKING_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.NEGATIVE)
    @allure.severity(Severity.CRITICAL)
    def test_get_booking_without_auth(
        self,
        booking_private_client_invalid: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Negative test: Attempt to retrieve booking without authentication.
        Should return 403 Forbidden.
        """
        booking_id = created_booking.response.bookingid
        allure.dynamic.title(f"GET /booking/{booking_id} - Retrieve booking without authentication (403)")
        response = booking_private_client_invalid.get_booking_api(booking_id)
        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)

    @allure.story(AllureStory.BOOKING_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.NEGATIVE)
    @allure.title("GET /booking/9999 - Retrieve non-existent booking (404)")
    @allure.severity(Severity.NORMAL)
    def test_get_booking_not_found(self, booking_private_client: PrivateBookingClient):
        """
        Negative test: Request booking with non-existent ID.
        Should return 404 Not Found.
        """
        response = booking_private_client.get_booking_api(9999)
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)

    @allure.story(AllureStory.BOOKING_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.NEGATIVE)
    @allure.title("GET /booking/one - Retrieve booking with invalid ID format (404)")
    @allure.severity(Severity.NORMAL)
    def test_get_booking_invalid_id_format(self, booking_private_client: PrivateBookingClient):
        """
        Negative test: Request booking with non-numeric ID in path.
        Should return 404 Not Found.
        """
        path = BookingRoutes.BOOKING_ID.format(id="one")
        response = booking_private_client.get(path)
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)

    @allure.story(AllureStory.BOOKING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_update_booking_success(
        self,
        booking_private_client: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Positive test: Successfully update existing booking.
        Validates update response and ensures data is correctly updated.
        """
        booking_id = created_booking.response.bookingid
        allure.dynamic.title(f"PUT /booking/{booking_id} - Update booking successfully")
        original_roomid = created_booking.request.roomid

        update_request = UpdateBookingRequestFactory.build(
            booking_id=booking_id,
            original_roomid=original_roomid
        )

        response = booking_private_client.update_booking_api(booking_id, update_request)
        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = UpdateBookingResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())

        assert_update_booking_response(update_request, response_data)

        # Verify update persisted
        get_response = booking_private_client.get_booking_api(booking_id)
        assert_status_code(get_response.status_code, HTTPStatus.OK)
        updated_booking = BookingSchema.model_validate_json(get_response.text)
        assert_booking(updated_booking, response_data.booking)

    @allure.story(AllureStory.BOOKING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_update_booking_high_level(
        self,
        booking_private_client: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Positive test: Use convenience method update_booking().
        Returns parsed Pydantic model UpdateBookingResponseSchema.
        """
        booking_id = created_booking.response.bookingid
        allure.dynamic.title(f"PUT /booking/{booking_id} - High-level method for updating booking")
        original_roomid = created_booking.request.roomid

        update_request = UpdateBookingRequestFactory.build(
            booking_id=booking_id,
            original_roomid=original_roomid
        )

        response_data = booking_private_client.update_booking(booking_id, update_request)
        assert_is_instance(response_data, UpdateBookingResponseSchema, "response_data")
        assert_update_booking_response(update_request, response_data)

        # Verify update persisted
        get_response = booking_private_client.get_booking_api(booking_id)
        assert_status_code(get_response.status_code, HTTPStatus.OK)
        updated_booking = BookingSchema.model_validate_json(get_response.text)
        assert_booking(updated_booking, response_data.booking)

    @allure.story(AllureStory.BOOKING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.severity(Severity.CRITICAL)
    def test_update_booking_without_auth(
        self,
        booking_private_client_invalid: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Negative test: Attempt to update booking without authentication.
        Should return 403 Forbidden.
        """
        booking_id = created_booking.response.bookingid
        allure.dynamic.title(f"PUT /booking/{booking_id} - Update booking without authentication (403)")
        original_roomid = created_booking.request.roomid

        update_request = UpdateBookingRequestFactory.build(
            booking_id=booking_id,
            original_roomid=original_roomid
        )

        response = booking_private_client_invalid.update_booking_api(booking_id, update_request)
        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)

    @allure.story(AllureStory.BOOKING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("PUT /booking/9999 - Update non-existent booking (404)")
    @allure.severity(Severity.NORMAL)
    def test_update_booking_not_found(self, booking_private_client: PrivateBookingClient):
        """
        Negative test: Update booking with non-existent ID.
        Should return 404 Not Found.
        """
        non_existent_id = 9999
        original_roomid = 1

        update_request = UpdateBookingRequestFactory.build(
            booking_id=non_existent_id,
            original_roomid=original_roomid
        )

        response = booking_private_client.update_booking_api(non_existent_id, update_request)
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)

    @allure.story(AllureStory.BOOKING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.severity(Severity.NORMAL)
    def test_update_booking_invalid_data(
        self,
        booking_private_client: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Negative test: Update booking with invalid data (empty firstname).
        Should return 400 Bad Request with validation error details.
        """
        booking_id = created_booking.response.bookingid
        allure.title(f"PUT /booking/{booking_id} - Update booking with empty firstname (400)")
        original_roomid = created_booking.request.roomid

        update_request = UpdateBookingRequestFactory.build(
            booking_id=booking_id,
            original_roomid=original_roomid
        )
        invalid_data = update_request.model_dump(mode="json")
        invalid_data["firstname"] = ""
        path = BookingRoutes.BOOKING_ID.format(id=booking_id)
        response = booking_private_client.put(path, json=invalid_data)
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)

        error_data = ValidationErrorSchema.model_validate_json(response.text)
        assert_validation_error(error_data, expected_fields=["firstname"])

    @allure.story(AllureStory.BOOKING_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_delete_booking_success(
        self,
        booking_private_client: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Positive test: Successfully delete a booking.
        Validates 202 Accepted status and verifies booking is no longer accessible.
        """
        booking_id = created_booking.response.bookingid
        allure.dynamic.title(f"DELETE /booking/{booking_id} - Delete booking successfully (202)")

        response = booking_private_client.delete_booking_api(booking_id)
        assert_status_code(response.status_code, HTTPStatus.ACCEPTED)

        get_response = booking_private_client.get_booking_api(booking_id)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)

        if get_response.text:
            error_data = BaseErrorResponse.model_validate_json(get_response.text)
            assert_base_error_response(error_data, expected_status=404)

    @allure.story(AllureStory.BOOKING_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY, AllureTag.NEGATIVE)
    @allure.severity(Severity.CRITICAL)
    def test_delete_booking_without_auth(
        self,
        booking_private_client_invalid: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Negative test: Attempt to delete booking without authentication.
        Should return 403 Forbidden.
        """
        booking_id = created_booking.response.bookingid
        allure.dynamic.title(f"DELETE /booking/{booking_id} - Delete booking without authentication (403)")

        response = booking_private_client_invalid.delete_booking_api(booking_id)
        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)

    @allure.story(AllureStory.BOOKING_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("DELETE /booking/9999 - Delete non-existent booking (404)")
    @allure.severity(Severity.NORMAL)
    def test_delete_booking_not_found(self, booking_private_client: PrivateBookingClient):
        """
        Negative test: Delete booking with non-existent ID.
        Should return 404 Not Found.
        """
        non_existent_id = 9999

        response = booking_private_client.delete_booking_api(non_existent_id)
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)

    @allure.story(AllureStory.BOOKING_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY, AllureTag.NEGATIVE)
    @allure.severity(Severity.NORMAL)
    def test_delete_booking_already_deleted(
        self,
        booking_private_client: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Negative test: Delete already deleted booking (idempotent operation).
        Should return 404 Not Found on second attempt.
        """
        booking_id = created_booking.response.bookingid
        allure.dynamic.title(f"DELETE /booking/{booking_id} - Delete already deleted booking (404)")

        first_response = booking_private_client.delete_booking_api(booking_id)
        assert_status_code(first_response.status_code, HTTPStatus.ACCEPTED)

        second_response = booking_private_client.delete_booking_api(booking_id)
        assert_status_code(second_response.status_code, HTTPStatus.NOT_FOUND)

    @allure.story(AllureStory.BOOKING_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_delete_booking_high_level(
        self,
        booking_private_client: PrivateBookingClient,
        created_booking: BookingFixture
    ):
        """
        Positive test: Use convenience method delete_booking().
        Method doesn't return a model (only validates status).
        """
        booking_id = created_booking.response.bookingid
        allure.dynamic.title(f"DELETE /booking/{booking_id} - High-level method for deleting booking")

        try:
            booking_private_client.delete_booking(booking_id)
        except Exception as e:
            pytest.fail(f"High-level delete_booking method raised exception: {e}")

        get_response = booking_private_client.get_booking_api(booking_id)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
