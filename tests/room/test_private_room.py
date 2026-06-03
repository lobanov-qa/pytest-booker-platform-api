from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.room.private_room_client import PrivateRoomClient
from clients.room.room_schema import RoomRequestSchema, RoomResponseSchema
from clients.room.routes import RoomRoutes
from data_factories.room_factory import RoomRequestFactory
from fixtures.room import RoomFixture
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import assert_status_code, assert_is_instance, assert_positive
from utils.assertions.room import (
    assert_create_room_response,
    assert_room,
    assert_get_room_response,
)
from utils.assertions.schema import validate_json_schema
from clients.errors_schema import ValidationErrorSchema
from utils.assertions.errors import assert_validation_error


@pytest.mark.room
@pytest.mark.regression
@allure.tag(AllureTag.ROOM)
@allure.epic(AllureEpic.ROOM)
@allure.feature(AllureFeature.ROOM_CRUD)
class TestPrivateRoomAPI:
    """
    Test suite for authenticated room operations.
    These tests require valid authentication tokens.
    """

    # ------------------------------------------------------------------
    # CREATE — positive
    # ------------------------------------------------------------------

    @pytest.mark.smoke
    @allure.story(AllureStory.ROOM_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("POST /room/ - Create room successfully (201)")
    @allure.severity(Severity.BLOCKER)
    def test_create_room_201(
        self,
        private_room_client: PrivateRoomClient,
        valid_room_request: RoomRequestSchema,
    ):
        """
        Positive test: Create room with full validation.
        Validates response structure and JSON schema compliance.
        """
        response = private_room_client.create_room_api(valid_room_request)
        assert_status_code(response.status_code, HTTPStatus.CREATED)
        response_data = RoomResponseSchema.model_validate_json(response.text)
        assert_create_room_response(valid_room_request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.ROOM_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("POST /room/ - High-level method for creating room")
    @allure.severity(Severity.NORMAL)
    def test_create_room_high_level(
        self,
        private_room_client: PrivateRoomClient,
        valid_room_request: RoomRequestSchema,
    ):
        """
        Positive test: Use convenience method create_room().
        Returns parsed Pydantic model RoomResponseSchema.
        """
        response_data = private_room_client.create_room(valid_room_request)
        assert_is_instance(response_data, RoomResponseSchema, "response_data")
        assert_positive(response_data.roomid, "roomid")
        assert_create_room_response(valid_room_request, response_data)

    # ------------------------------------------------------------------
    # READ — verify get matches create
    # ------------------------------------------------------------------

    @pytest.mark.smoke
    @allure.story(AllureStory.ROOM_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("GET /room/{id} - Get room matches created room data")
    @allure.severity(Severity.CRITICAL)
    def test_get_room_matches_created(
        self,
        private_room_client: PrivateRoomClient,
        created_room: RoomFixture,
    ):
        """
        Positive test: Verify that GET /room/{id} returns data matching the created room.
        Uses assert_get_room_response for validation.
        """
        room_id = created_room.room_id
        allure.dynamic.title(f"GET /room/{room_id} - Get room matches created room data")

        get_response_data = private_room_client.get_room(room_id)
        assert_get_room_response(get_response_data, created_room.response)

    # ------------------------------------------------------------------
    # UPDATE — positive
    # ------------------------------------------------------------------

    @pytest.mark.smoke
    @allure.story(AllureStory.ROOM_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_update_room_200(
        self,
        private_room_client: PrivateRoomClient,
        created_room: RoomFixture,
    ):
        """
        Positive test: Successfully update existing room.
        Validates update response and ensures data is correctly updated.
        """
        room_id = created_room.room_id
        allure.dynamic.title(f"PUT /room/{room_id} - Update room successfully (200)")

        update_request = RoomRequestFactory.build()

        response = private_room_client.update_room_api(room_id, update_request)
        assert_status_code(response.status_code, HTTPStatus.ACCEPTED)
        response_data = RoomResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_create_room_response(update_request, response_data)

        # Verify update persisted
        get_response = private_room_client.get_room_api(room_id)
        assert_status_code(get_response.status_code, HTTPStatus.OK)
        updated_room = RoomResponseSchema.model_validate_json(get_response.text)
        assert_room(updated_room, response_data)

    @allure.story(AllureStory.ROOM_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_update_room_high_level(
        self,
        private_room_client: PrivateRoomClient,
        created_room: RoomFixture,
    ):
        """
        Positive test: Use convenience method update_room().
        Returns parsed Pydantic model RoomResponseSchema.
        """
        room_id = created_room.room_id
        allure.dynamic.title(f"PUT /room/{room_id} - High-level method for updating room")

        update_request = RoomRequestFactory.build()
        response_data = private_room_client.update_room(room_id, update_request)
        assert_is_instance(response_data, RoomResponseSchema, "response_data")
        assert_positive(response_data.roomid, "roomid")

        # Verify update persisted
        get_response = private_room_client.get_room(room_id)
        assert_room(get_response, response_data)

    # ------------------------------------------------------------------
    # DELETE — positive
    # ------------------------------------------------------------------

    @pytest.mark.smoke
    @allure.story(AllureStory.ROOM_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_delete_room_202(
        self,
        private_room_client: PrivateRoomClient,
        created_room: RoomFixture,
    ):
        """
        Positive test: Successfully delete a room.
        Validates 202 Accepted status and verifies room returns 500 after deletion
        (API returns 500 for non-existent room IDs).
        """
        room_id = created_room.room_id
        allure.dynamic.title(f"DELETE /room/{room_id} - Delete room successfully (202)")

        response = private_room_client.delete_room_api(room_id)
        assert_status_code(response.status_code, HTTPStatus.ACCEPTED)

        # Verify room is gone — API returns 500 for deleted/non-existent rooms
        get_response = private_room_client.get_room_api(room_id)
        assert_status_code(get_response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    @allure.story(AllureStory.ROOM_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_delete_room_high_level(
        self,
        private_room_client: PrivateRoomClient,
        created_room: RoomFixture,
    ):
        """
        Positive test: Use convenience method delete_room().
        Method doesn't return a model (only validates status).
        """
        room_id = created_room.room_id
        allure.dynamic.title(f"DELETE /room/{room_id} - High-level method for deleting room")

        try:
            private_room_client.delete_room(room_id)
        except Exception as e:
            pytest.fail(f"High-level delete_room method raised exception: {e}")

        # Verify room is gone — API returns 500 for deleted/non-existent rooms
        get_response = private_room_client.get_room_api(room_id)
        assert_status_code(get_response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    # ------------------------------------------------------------------
    # NEGATIVE — unauthorized
    # ------------------------------------------------------------------

    @allure.story(AllureStory.ROOM_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("POST /room/ - Create room without authentication (403)")
    @allure.severity(Severity.CRITICAL)
    def test_create_room_unauthorized_403(
        self,
        private_room_client_invalid: PrivateRoomClient,
        valid_room_request: RoomRequestSchema,
    ):
        """
        Negative test: Attempt to create room without authentication.
        Should return 403 Forbidden.
        """
        response = private_room_client_invalid.create_room_api(valid_room_request)
        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)

    @allure.story(AllureStory.ROOM_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("PUT /room/1 - Update room without authentication (403)")
    @allure.severity(Severity.CRITICAL)
    def test_update_room_unauthorized_403(
        self,
        private_room_client_invalid: PrivateRoomClient,
    ):
        """
        Negative test: Attempt to update room without authentication.
        Should return 403 Forbidden.
        """
        update_request = RoomRequestFactory.build()
        response = private_room_client_invalid.update_room_api(1, update_request)
        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)

    @allure.story(AllureStory.ROOM_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("DELETE /room/1 - Delete room without authentication (403)")
    @allure.severity(Severity.CRITICAL)
    def test_delete_room_unauthorized_403(
        self,
        private_room_client_invalid: PrivateRoomClient,
    ):
        """
        Negative test: Attempt to delete room without authentication.
        Should return 403 Forbidden.
        """
        response = private_room_client_invalid.delete_room_api(1)
        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)

    # ------------------------------------------------------------------
    # NEGATIVE — validation errors
    # ------------------------------------------------------------------

    @allure.story(AllureStory.ROOM_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("POST /room/ - Create room without roomPrice (400)")
    @allure.severity(Severity.NORMAL)
    def test_create_room_without_room_price_400(
        self,
        private_room_client: PrivateRoomClient,
    ):
        """
        Negative test: Create room without required roomPrice field.
        Real API requires roomPrice >= 1; returns 400 with ValidationErrorSchema.
        Uses assert_validation_error for structured error validation.
        """
        # Send raw JSON to bypass Pydantic validation (roomPrice=0 fails Field(ge=1))
        response = private_room_client.client.post(
            RoomRoutes.ROOT,
            json={"roomName": "Test", "type": "Single", "roomPrice": 0}
        )
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        error_data = ValidationErrorSchema.model_validate_json(response.text)
        assert_validation_error(error_data)

    # ------------------------------------------------------------------
    # NEGATIVE — not found
    # ------------------------------------------------------------------

    @allure.story(AllureStory.ROOM_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("PUT /room/9999 - Update non-existent room (404)")
    @allure.severity(Severity.NORMAL)
    def test_update_room_not_found_404(
        self,
        private_room_client: PrivateRoomClient,
    ):
        """
        Negative test: Update room with non-existent ID.
        Should return 404 Not Found.
        """
        update_request = RoomRequestFactory.build()
        response = private_room_client.update_room_api(9999, update_request)
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)

    @allure.story(AllureStory.ROOM_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("DELETE /room/9999 - Delete non-existent room (404)")
    @allure.severity(Severity.NORMAL)
    def test_delete_room_not_found_404(
        self,
        private_room_client: PrivateRoomClient,
    ):
        """
        Negative test: Delete room with non-existent ID.
        Should return 404 Not Found.
        """
        response = private_room_client.delete_room_api(9999)
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)