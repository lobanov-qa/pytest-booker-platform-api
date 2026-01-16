from typing import Optional
from utils.fakers import fake
from clients.booking.booking_schema import UnavailableDatesQuerySchema, GetSummaryQuerySchema


class UnavailableDatesQueryFactory:
    """
    Factory for creating query parameters for checking room availability.
    Uses methods from fake for consistency.
    """

    @classmethod
    def build(
            cls,
            checkin: Optional[str] = None,
            checkout: Optional[str] = None,
            **overrides
    ) -> UnavailableDatesQuerySchema:
        """
        Creates a valid UnavailableDatesQuerySchema object.
        """
        if checkin is None or checkout is None:
            dates = fake.booking_dates()
            checkin = checkin or dates["checkin"]
            checkout = checkout or dates["checkout"]

        base_data = {
            "checkin": checkin,
            "checkout": checkout,
        }

        base_data.update(overrides)
        return UnavailableDatesQuerySchema(**base_data)




class GetSummaryQueryFactory:
    """
    Factory for creating query parameters for obtaining a summary of bookings.
    """

    @classmethod
    def build(
            cls,
            roomid: Optional[int] = None,
            **overrides
    ) -> GetSummaryQuerySchema:
        """
        Creates a valid GetSummaryQuerySchema object.
        """
        room_id = roomid or fake.room_id()

        base_data = {
            "roomid": str(room_id),
        }

        base_data.update(overrides)
        return GetSummaryQuerySchema(**base_data)

