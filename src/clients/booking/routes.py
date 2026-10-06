from enum import StrEnum


class BookingRoutes(StrEnum):
    """Endpoints of the booking-service."""

    ROOT = "/"
    UNAVAILABLE = "/unavailable"
    SUMMARY = "/summary"
    BOOKING_ID = "/{id}"

    def __str__(self) -> str:
        return self.value
