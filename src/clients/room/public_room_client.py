import allure

from typing import Optional
from httpx import Response

from clients.api_client import APIClient
from clients.room.room_schema import (
    RoomResponseSchema,
    RoomsResponseSchema,
    GetRoomsQuerySchema
)
from clients.room.routes import RoomRoutes
from clients.api_coverage import tracker_room


class PublicRoomClient(APIClient):
    """
    Client for /room/ API.

    Supports both raw responses (_api methods) for negative tests
    and parsed models (domain methods) for positive flows.
    """

    def __init__(self, base_url: str, timeout: float, event_hooks=None, **kwargs):
        """
        :param base_url: Room service base URL.
        :param timeout: Request timeout in seconds.
        :param event_hooks: Optional hooks (logging, etc.).
        :param kwargs: Passed to APIClient.
        """
        super().__init__(base_url=base_url, timeout=timeout, event_hooks=event_hooks, **kwargs)



    @allure.step("Get all rooms")
    @tracker_room.track_coverage_httpx(RoomRoutes.ROOT)
    def get_rooms_api(self, query: Optional[GetRoomsQuerySchema] = None) -> Response:
        """
        Get all rooms optionally filtered by check-in/check-out dates (raw response).
        :param query: Optional date filter.
        :return: HTTP response.
        """
        return self.get(RoomRoutes.ROOT, params=query.model_dump(exclude_none=True) if query else None)

    def get_rooms(self, query: Optional[GetRoomsQuerySchema] = None) -> RoomsResponseSchema:
        """
        Get all rooms and return parsed model (expects success).
        :param query: Optional date filter.
        :return: Parsed response with list of rooms.
        :raises HTTPStatusError: If status != 2xx.
        """
        return self.parse_response(self.get_rooms_api(query), RoomsResponseSchema)

    @allure.step("Get room by ID {roomid}")
    @tracker_room.track_coverage_httpx(RoomRoutes.ROOM_ID)
    def get_room_api(self, roomid: int) -> Response:
        """
        Get a specific room by ID (raw response).
        :param roomid: Room identifier.
        :return: HTTP response.
        """
        path = RoomRoutes.ROOM_ID.format(id=roomid)
        return self.get(path)

    def get_room(self, roomid: int) -> RoomResponseSchema:
        """
        Get a specific room and return parsed model (expects success).
        :param roomid: Room identifier.
        :return: Parsed room model.
        :raises HTTPStatusError: If status != 2xx.
        """
        response = self.get_room_api(roomid)
        return self.parse_response(response, RoomResponseSchema)