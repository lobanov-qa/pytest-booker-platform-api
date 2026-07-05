from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.booking.booking_schema import GetSummaryQuerySchema
from clients.report.report_schema import ReportSchema
from data_factories.booking_factory import CreateBookingRequestFactory
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import (
    assert_status_code,
    assert_is_instance,
    assert_length_equal,
)


@pytest.mark.e2e
@pytest.mark.smoke
@allure.epic(AllureEpic.E2E)
@allure.feature(AllureFeature.FULL_AUDIT_TRAIL)
@allure.tag(AllureTag.E2E, AllureTag.AUDIT)
class TestFullHotelAudit:
    """Complete hotel audit trail across all services."""

    @allure.story(AllureStory.ROOM_CREATION_IN_FLOW)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Admin creates a room and it appears in the public list")
    @allure.severity(Severity.BLOCKER)
    def test_room_creation_and_visibility(
        self,
        public_room_client,
        created_room,
    ):
        room_id = created_room.room_id

        room_list_resp = public_room_client.get_rooms_api()
        assert_status_code(room_list_resp.status_code, HTTPStatus.OK)
        rooms = room_list_resp.json()["rooms"]
        room_ids = [r["roomid"] for r in rooms]
        assert room_id in room_ids, f"Room {room_id} not found in public list"

    @allure.story(AllureStory.BOOKING_WITHIN_AUDIT)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Guest books the room and admin verifies the booking")
    @allure.severity(Severity.BLOCKER)
    def test_booking_creation_and_verification(
        self,
        booking_client,
        booking_private_client,
        created_room,
    ):
        room_id = created_room.room_id
        booking_request = CreateBookingRequestFactory.build(roomid=room_id)
        create_resp = booking_client.create_booking_api(booking_request)
        assert_status_code(create_resp.status_code, HTTPStatus.CREATED)
        body = create_resp.json()
        booking_id = body["bookingid"]

        summary_query = GetSummaryQuerySchema(roomid=str(room_id))
        summary_resp = booking_client.get_summary_api(summary_query)
        assert_status_code(summary_resp.status_code, HTTPStatus.OK)

        get_resp = booking_private_client.get_booking_api(booking_id)
        assert_status_code(get_resp.status_code, HTTPStatus.OK)
        booking_detail = get_resp.json()
        assert booking_detail["roomid"] == room_id, "Booking roomid should match created room"

    @allure.story(AllureStory.MESSAGE_WITHIN_AUDIT)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Guest sends a message, admin reads it and marks as read")
    @allure.severity(Severity.BLOCKER)
    def test_message_flow(
        self,
        public_message_client,
        private_message_client,
        created_message,
    ):
        message_id = created_message.message_id

        list_resp = public_message_client.get_messages_api()
        assert_status_code(list_resp.status_code, HTTPStatus.OK)
        messages = list_resp.json()
        msg_ids = [m["id"] for m in messages.get("messages", [])]
        assert message_id in msg_ids, f"Message {message_id} not found in list"

        mark_resp = private_message_client.mark_read_api(message_id)
        assert_status_code(mark_resp.status_code, HTTPStatus.ACCEPTED)

        count_resp = public_message_client.get_count_api()
        assert_status_code(count_resp.status_code, HTTPStatus.OK)
        count_body = count_resp.json()
        assert_is_instance(count_body.get("count"), int, "messages count")

    @allure.story(AllureStory.BOOKING_CANCELLATION)
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.title("Admin cancels the booking and verifies the report is updated")
    @allure.severity(Severity.CRITICAL)
    def test_cancellation_and_report(
        self,
        booking_client,
        booking_private_client,
        report_public_client,
        report_private_client,
        created_room,
    ):
        room_id = created_room.room_id
        booking_request = CreateBookingRequestFactory.build(roomid=room_id)
        create_resp = booking_client.create_booking_api(booking_request)
        assert_status_code(create_resp.status_code, HTTPStatus.CREATED)
        booking_id = create_resp.json()["bookingid"]

        all_bookings_resp = booking_private_client.get_bookings_api()
        assert_status_code(all_bookings_resp.status_code, HTTPStatus.OK)
        all_bookings = all_bookings_resp.json()
        all_ids = [b["bookingid"] for b in all_bookings["bookings"]]
        assert booking_id in all_ids, f"Booking {booking_id} not found in all bookings"

        delete_resp = booking_private_client.delete_booking_api(booking_id)
        assert_status_code(delete_resp.status_code, HTTPStatus.ACCEPTED)

        get_deleted_resp = booking_private_client.get_booking_api(booking_id)
        assert_status_code(get_deleted_resp.status_code, HTTPStatus.NOT_FOUND)

        report = report_public_client.get_room_report(room_id)
        assert_is_instance(report, ReportSchema, "report")
        assert_length_equal(report.report, 0, "report entries")

        all_report = report_private_client.get_all_reports()
        assert_is_instance(all_report, ReportSchema, "all_report")
        assert_is_instance(all_report.report, list, "all_report entries")
