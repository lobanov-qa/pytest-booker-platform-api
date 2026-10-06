from enum import StrEnum


class RoomRoutes(StrEnum):
    """Endpoints of the room-service."""

    ROOT = "/"
    ROOM_ID = "/{id}"

    def __str__(self):
        return self.value
