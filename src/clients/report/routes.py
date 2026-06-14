from enum import StrEnum


class ReportRoutes(StrEnum):
    ROOT = "/"
    ROOM_REPORT = "/room/{id}"

    def __str__(self):
        return self.value
