from enum import StrEnum


class BookingRoutes(StrEnum):
    UNAVAILABLE = "/unavailable"
    SUMMARY = "/summary"
    BOOKING_ID = "/{id}"


    def __str__(self):
        return self.value