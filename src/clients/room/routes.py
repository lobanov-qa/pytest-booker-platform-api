from enum import StrEnum


class RoomRoutes(StrEnum):
    ROOT = "/"
    ROOM_ID = "/{id}"


    def __str__(self):
        return self.value