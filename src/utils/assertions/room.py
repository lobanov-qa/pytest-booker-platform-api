import allure

from clients.room.room_schema import RoomRequestSchema, RoomResponseSchema
from utils.assertions.base import assert_equal, assert_is_instance, assert_positive
from utils.logger import get_logger

logger = get_logger("ROOM_ASSERTIONS")


@allure.step("Check create room response")
def assert_create_room_response(request: RoomRequestSchema, response: RoomResponseSchema):
    """
    Verifies that the room creation response matches the request.

    :param request: Initial request to create a room.
    :param response: API response with room data.
    :raises AssertionError: If at least one field does not match.
    """
    logger.info("Check create room response")
    assert_positive(response.roomid, "roomid not positive")
    assert_equal(response.room_name, request.room_name, "room_name")
    assert_equal(response.room_type, request.room_type, "room_type")

    if request.accessible is not None:
        assert_equal(response.accessible, request.accessible, "accessible")
    if request.image is not None:
        assert_equal(response.image, request.image, "image")
    if request.description is not None:
        assert_equal(response.description, request.description, "description")
    if request.features is not None:
        assert_equal(response.features, request.features, "features")
    if request.room_price is not None:
        assert_equal(response.room_price, request.room_price, "room_price")


@allure.step("Check room")
def assert_room(actual: RoomResponseSchema, expected: RoomResponseSchema):
    """
    Checks that the actual room data matches the expected one.

    :param actual: Actual room data.
    :param expected: Expected room data.
    :raises AssertionError: If at least one field does not match.
    """
    logger.info("Check room")
    assert_equal(actual.roomid, expected.roomid, "roomid")
    assert_equal(actual.room_name, expected.room_name, "room_name")
    assert_equal(actual.room_type, expected.room_type, "room_type")
    assert_equal(actual.accessible, expected.accessible, "accessible")
    assert_equal(actual.image, expected.image, "image")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.features, expected.features, "features")
    assert_equal(actual.room_price, expected.room_price, "room_price")


@allure.step("Check get room response")
def assert_get_room_response(
    get_response: RoomResponseSchema,
    create_response: RoomResponseSchema
):
    """
    Checks that the response when receiving a room matches the response when creating it.

    :param get_response: API response when requesting room data.
    :param create_response: Room data from creation response.
    :raises AssertionError: If room data does not match.
    """
    logger.info("Check get room response")
    assert_room(get_response, create_response)


@allure.step("Check rooms list contains room")
def assert_rooms_list_contains(rooms: list[RoomResponseSchema], expected_room: RoomResponseSchema):
    """
    Checks that the list of rooms contains the expected room.

    :param rooms: List of rooms from API response.
    :param expected_room: Expected room data.
    :raises AssertionError: If the room is not found or data does not match.
    """
    logger.info("Check rooms list contains room")
    assert_is_instance(rooms, list, "rooms")

    found_room = None
    for room in rooms:
        if room.roomid == expected_room.roomid:
            found_room = room
            break

    assert found_room is not None, (
        f"Expected room with id {expected_room.roomid} not found in response. "
        f"Found room ids: {[r.roomid for r in rooms]}"
    )

    assert_room(found_room, expected_room)


