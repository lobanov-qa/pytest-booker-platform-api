from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.room.public_room_client import PublicRoomClient
from clients.room.private_room_client import PrivateRoomClient
from clients.room.room_schema import (
    RoomResponseSchema,
    RoomsResponseSchema,
    GetRoomsQuerySchema,
)
from clients.errors_schema import BaseErrorResponse
from fixtures.room import RoomFixture
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import (
    assert_status_code,
    assert_positive,
    assert_is_instance,
    assert_equal,
)
from utils.assertions.errors import assert_base_error_response
from utils.assertions.room import (
    assert_get_room_response,
    assert_rooms_list_contains,
)
from utils.assertions.schema import validate_json_schema


@pytest.mark.room
@pytest.mark.regression
@allure.tag(AllureTag.ROOM)
@allure.epic(AllureEpic.ROOM)
@allure.feature(AllureFeature.ROOM_AVAILABILITY)
class TestPublicRoomAPI:
    """
    Test suite for public room operations (no authentication required).
    Covers get all rooms, get room by ID, and filtering by dates.
    """

    @pytest.mark.smoke
    @allure.story(AllureStory.ROOM_LIST)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /room/ - Get all rooms successfully (200)")
    @allure.severity(Severity.BLOCKER)
    def test_get_rooms_returns_200(self, public_room_client: PublicRoomClient):
        """
        Positive test: Retrieve all rooms without any filters.
        Validates response structure and JSON schema compliance.
        """
        response = public_room_client.get_rooms_api()
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = RoomsResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_is_instance(response_data.rooms, list, "rooms")

    @allure.story(AllureStory.ROOM_LIST)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /room/ - Get rooms filtered by dates")
    @allure.severity(Severity.CRITICAL)
    def test_get_rooms_with_dates(self, public_room_client: PublicRoomClient):
        """
        Positive test: Retrieve rooms filtered by check-in and check-out dates.
        """
        query = GetRoomsQuerySchema(checkin="2025-12-01", checkout="2025-12-10")
        response = public_room_client.get_rooms_api(query)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = RoomsResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_is_instance(response_data.rooms, list, "rooms")

    @pytest.mark.smoke
    @allure.story(AllureStory.ROOM_LIST)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /room/ - High-level method for getting all rooms")
    @allure.severity(Severity.NORMAL)
    def test_get_rooms_high_level(self, public_room_client: PublicRoomClient):
        """
        Positive test: Use convenience method get_rooms().
        Returns parsed Pydantic model RoomsResponseSchema.
        """
        response_data = public_room_client.get_rooms()
        assert_is_instance(response_data, RoomsResponseSchema, "response_data")
        assert_is_instance(response_data.rooms, list, "rooms")
        for room in response_data.rooms:
            assert_positive(room.roomid, "roomid")

    @pytest.mark.smoke
    @allure.story(AllureStory.ROOM_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("GET /room/1 - Get room by ID successfully (200)")
    @allure.severity(Severity.BLOCKER)
    def test_get_room_by_id(self, public_room_client: PublicRoomClient):
        """
        Positive test: Retrieve a specific room by ID.
        Validates response structure and JSON schema compliance.
        """
        room_id = 1
        response = public_room_client.get_room_api(room_id)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = RoomResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_positive(response_data.roomid, "roomid")

    @pytest.mark.smoke
    @allure.story(AllureStory.ROOM_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("GET /room/1 - High-level method for getting room by ID")
    @allure.severity(Severity.NORMAL)
    def test_get_room_high_level(self, public_room_client: PublicRoomClient):
        """
        Positive test: Use convenience method get_room().
        Returns parsed Pydantic model RoomResponseSchema.
        """
        room_id = 1
        response_data = public_room_client.get_room(room_id)
        assert_is_instance(response_data, RoomResponseSchema, "response_data")
        assert_positive(response_data.roomid, "roomid")

    @allure.story(AllureStory.ROOM_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.NEGATIVE)
    @allure.title("GET /room/9999 - Retrieve non-existent room (500)")
    @allure.severity(Severity.NORMAL)
    def test_get_room_not_found_500(self, public_room_client: PublicRoomClient):
        """
        Negative test: Request room with non-existent ID.
        Real API returns 500 Internal Server Error for non-existent room IDs.
        """
        response = public_room_client.get_room_api(9999)
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        error_data = BaseErrorResponse.model_validate_json(response.text)
        assert_base_error_response(error_data, expected_status=500, path_contains="/")

    @allure.story(AllureStory.ROOM_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.NEGATIVE)
    @allure.title("GET /room/0 - Retrieve room with invalid ID 0 (500)")
    @allure.severity(Severity.NORMAL)
    def test_get_room_invalid_id_500(self, public_room_client: PublicRoomClient):
        """
        Negative test: Request room with ID=0 (must be >=1).
        Real API returns 500 Internal Server Error.
        """
        response = public_room_client.get_room_api(0)
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        error_data = BaseErrorResponse.model_validate_json(response.text)
        assert_base_error_response(error_data, expected_status=500, path_contains="/")

    @allure.story(AllureStory.ROOM_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.NEGATIVE)
    @pytest.mark.parametrize("invalid_id", [-1, -999])
    @allure.title("GET /room/{invalid_id} - Retrieve room with negative ID (404)")
    @allure.severity(Severity.NORMAL)
    def test_get_room_invalid_id_negative(
        self, public_room_client: PublicRoomClient, invalid_id: int
    ):
        """
        Negative test: Request room with negative ID.
        Real API returns 404 Not Found for negative IDs.
        """
        response = public_room_client.get_room_api(invalid_id)
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)
        error_data = BaseErrorResponse.model_validate_json(response.text)
        assert_base_error_response(error_data, expected_status=404, path_contains="/")

    @pytest.mark.smoke
    @allure.story(AllureStory.ROOM_LIST)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /room/ - Verify created room appears in rooms list")
    @allure.severity(Severity.NORMAL)
    def test_get_rooms_contains_created_room(
        self,
        public_room_client: PublicRoomClient,
        private_room_client: PrivateRoomClient,
        created_room: RoomFixture,
    ):
        """
        Positive test: Verify that a newly created room appears in the rooms list.
        Uses assert_rooms_list_contains for validation.
        """
        response_data = public_room_client.get_rooms()
        assert_rooms_list_contains(response_data.rooms, created_room.response)

    @pytest.mark.smoke
    @allure.story(AllureStory.ROOM_LIST)
    @allure.tag(AllureTag.GET_ENTITIES, AllureTag.NEGATIVE)
    @allure.title("GET /room/ - Get rooms with invalid date format (500)")
    @allure.severity(Severity.MINOR)
    def test_get_rooms_invalid_dates_500(self, public_room_client: PublicRoomClient):
        """
        Negative test: Get rooms with invalid date format.
        API returns 500 INTERNAL_SERVER_ERROR.
        """
        params = {"checkin": "2025/12/01", "checkout": "2025/12/10"}
        response = public_room_client.get("/", params=params)
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        error_data = BaseErrorResponse.model_validate_json(response.text)
        assert_base_error_response(error_data, expected_status=500, path_contains="/")