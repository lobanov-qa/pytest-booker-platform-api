from enum import StrEnum


class ReportRoutes(StrEnum):
    """Endpoints of the report-service."""

    ROOT = "/"
    ROOM_REPORT = "/room/{id}"

    def __str__(self) -> str:
        return self.value
