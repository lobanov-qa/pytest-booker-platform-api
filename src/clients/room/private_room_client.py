import allure
from httpx import Response, Cookies

from clients.api_client import APIClient
from clients.room.room_schema import (
    RoomRequestSchema,
    RoomResponseSchema,
)
from clients.room.routes import RoomRoutes
from clients.api_coverage import tracker_room


class PrivateRoomClient(APIClient):
    """
    Private client for the room API.

    Supports raw responses (_api methods) for full control in negative tests,
    and high-level parsed methods (returning Pydantic models) for positive flows.
    Designed to be used with authenticated session cookies.
    """

    def __init__(self, base_url: str, timeout: float, cookies: Cookies, event_hooks=None, **kwargs):
        """
        :param base_url: Base URL of the room service (e.g., http://localhost:3001).
        :param timeout: Request timeout in seconds.
        :param cookies: Session cookies obtained via authentication (e.g., from AuthClient.login).
        :param event_hooks: Optional hooks for logging, cURL printing, etc.
        :param kwargs: Additional arguments passed to APIClient.
        """
        super().__init__(base_url=base_url, timeout=timeout, cookies=cookies, event_hooks=event_hooks, **kwargs)

    @allure.step("Create room")
    @tracker_room.track_coverage_httpx(RoomRoutes.ROOT)
    def create_room_api(self, request: RoomRequestSchema) -> Response:
        """
        Create a new room (raw response).
        :param request: Room data (room_name, type required).
        :return: Raw HTTP response.
        """
        return self.post(RoomRoutes.ROOT, json=request.model_dump(mode="json", by_alias=True, exclude_none=True))

    def create_room(self, request: RoomRequestSchema) -> RoomResponseSchema:
        """
        Create a new room and return parsed model (expects success).
        :param request: Room data.
        :return: Parsed room model with roomid.
        :raises HTTPStatusError: If status != 2xx.
        """
        response = self.create_room_api(request)
        return self.parse_response(response, RoomResponseSchema)

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

    @allure.step("Update room by ID {roomid}")
    @tracker_room.track_coverage_httpx(RoomRoutes.ROOM_ID)
    def update_room_api(self, roomid: int, request: RoomRequestSchema) -> Response:
        """
        Update an existing room (raw response).
        :param roomid: ID of the room to update.
        :param request: Updated room data.
        :return: Raw HTTP response.
        """
        path = RoomRoutes.ROOM_ID.format(id=roomid)
        return self.put(path, json=request.model_dump(mode="json", by_alias=True, exclude_none=True))

    def update_room(self, roomid: int, request: RoomRequestSchema) -> RoomResponseSchema:
        """
        Update a room and return parsed model (expects success).
        :param roomid: ID of the room.
        :param request: Updated room data.
        :return: Parsed room model.
        :raises HTTPStatusError: If status != 2xx.
        """
        response = self.update_room_api(roomid, request)
        return self.parse_response(response, RoomResponseSchema)

    @allure.step("Delete room by ID {roomid}")
    @tracker_room.track_coverage_httpx(RoomRoutes.ROOM_ID)
    def delete_room_api(self, roomid: int) -> Response:
        """
        Delete a room by ID (raw response).
        :param roomid: ID of the room to delete.
        :return: Raw HTTP response.
        """
        path = RoomRoutes.ROOM_ID.format(id=roomid)
        return self.delete(path)

    def delete_room(self, roomid: int) -> None:
        """
        Delete a room by ID (expects success).
        :param roomid: ID of the room.
        :raises HTTPStatusError: If status != 2xx.
        """
        response = self.delete_room_api(roomid)
        response.raise_for_status()