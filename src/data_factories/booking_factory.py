from datetime import date

from utils.fakers import fake
from clients.booking.booking_schema import CreateBookingRequestSchema, BookingDates, UnavailableDatesQuerySchema


class CreateBookingRequestFactory:
    """
    Factory for creating a valid reservation request.
    Supports overriding any fields via **overrides.
    """

    @classmethod
    def build(cls, **overrides) -> CreateBookingRequestSchema:
        """
        Creates a valid CreateBookingRequestSchema object.
        :param overrides: Fields to override, for example firstname="Test".
        :return: Ready schema object.
        """
        
        checkin_str, checkout_str = fake.booking_dates().values() 
        checkin = date.fromisoformat(checkin_str)
        checkout = date.fromisoformat(checkout_str)
        booking_dates = BookingDates(checkin=checkin, checkout=checkout)

        base_data = {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "depositpaid": fake.deposit_paid(),
            "roomid": fake.room_id(),
            "bookingdates": booking_dates,
            "email": fake.email(),
            "phone": fake.phone(),
        }

        base_data.update(overrides)

        return CreateBookingRequestSchema(**base_data)



