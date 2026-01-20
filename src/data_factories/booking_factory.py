from datetime import date
from typing import Optional

from utils.fakers import fake
from clients.booking.booking_schema import CreateBookingRequestSchema, BookingDates, UpdateBookingRequestSchema


class CreateBookingRequestFactory:
    """
    Factory for creating valid new booking requests.
    """
    
    @classmethod
    def build(cls, **overrides) -> CreateBookingRequestSchema:
        """
        Creates a valid CreateBookingRequestSchema object.
        
        Args:
            **overrides: Fields to override, e.g., firstname="Test".
            
        Returns:
            Ready-to-use schema object for POST /booking.
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

class UpdateBookingRequestFactory:
    """
    Factory for creating valid update booking requests.
    
    IMPORTANT: 
    - bookingid is required and must match existing booking
    - roomid is required by API but will be ignored (returns original)
    - bookingdates is required (API returns 500 if missing)
    """
    
    @classmethod
    def build(
        cls,
        booking_id: int,
        original_roomid: Optional[int] = None,
        **overrides
    ) -> UpdateBookingRequestSchema:
        """
        Creates update request for an existing booking.
        
        Args:
            booking_id: ID of existing booking to update (REQUIRED).
            original_roomid: Original roomid (will be used if roomid not in overrides).
            **overrides: Fields to override.
            
        Returns:
            Valid UpdateBookingRequestSchema ready for PUT request.

        """

        checkin_str, checkout_str = fake.booking_dates().values()
        checkin = date.fromisoformat(checkin_str)
        checkout = date.fromisoformat(checkout_str)
        booking_dates = BookingDates(checkin=checkin, checkout=checkout)
        
        base_data = {
            "bookingid": booking_id,
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "depositpaid": fake.deposit_paid(),
            "bookingdates": booking_dates,
            "email": fake.email(),
            "phone": fake.phone(),
        }
        
        if "roomid" not in overrides and original_roomid is not None:
            base_data["roomid"] = original_roomid
        elif "roomid" not in overrides:
            base_data["roomid"] = fake.room_id()
        
        base_data.update(overrides)
        
        return UpdateBookingRequestSchema(**base_data)



