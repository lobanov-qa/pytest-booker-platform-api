from pydantic import BaseModel, Field, EmailStr, field_validator, RootModel, ConfigDict
from typing import Annotated, Optional, List
from datetime import date

from utils.validators import validate_date_range, validate_stringified_positive_int


class BookingDates(BaseModel):
    """
    Schema for booking dates (check-in and check-out).
    Validates that check-out is after check-in.
    """
    checkin: date
    checkout: date

    @field_validator("checkout")
    @classmethod
    def check_checkout_after_checkin(cls, v: date, info) -> date:
        checkin = info.data.get("checkin")
        if checkin:
            validate_date_range(checkin, v)
        return v


class BookingSchema(BaseModel):
    """
    Schema for a full booking record.
    """
    bookingid: int
    depositpaid: bool
    roomid: Annotated[int, Field(ge=1, description="Room ID, minimum 1")]
    firstname: Annotated[str, Field(min_length=3, max_length=18)]
    lastname: Annotated[str, Field(min_length=3, max_length=30)]
    bookingdates: BookingDates


class GetBookingQuerySchema(BaseModel):
    """
    Schema for GET /bookings — get all bookings or filter by roomid.
    roomid is optional: if not provided, returns all bookings.
    """
    roomid: Optional[str] = None

    @field_validator("roomid")
    @classmethod
    def validate_roomid(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        return validate_stringified_positive_int(v)


class GetBookingsResponseSchema(BaseModel):
    """
    Schema for response containing a list of bookings.
    """
    bookings: List[BookingSchema]


class GetBookingResponseSchema(BaseModel):
    """
    Schema for response containing a single booking.
    """
    booking: BookingSchema


class CreateBookingRequestSchema(BaseModel):
    """
    Schema for creating a new booking.
    """
    depositpaid: bool
    roomid: Annotated[int, Field(ge=1, description="Room ID, minimum 1")]
    firstname: Annotated[str, Field(min_length=3, max_length=18)]
    lastname: Annotated[str, Field(min_length=3, max_length=30)]
    bookingdates: BookingDates
    email: Optional[EmailStr] = None
    phone: Optional[Annotated[str, Field(min_length=11, max_length=21)]] = None


class CreateBookingResponseSchema(BaseModel):
    """
    Schema for response after creating a booking.
    """
    bookingid: int
    booking: BookingSchema


class UpdateBookingRequestSchema(BaseModel):
    """
    Schema for updating an existing booking (partial update).
    All fields are optional.
    """
    depositpaid: Optional[bool] = None
    roomid: Optional[int] = Field(None, ge=1)
    firstname: Optional[str] = Field(None, min_length=3, max_length=18)
    lastname: Optional[str] = Field(None, min_length=3, max_length=30)
    bookingdates: Optional[BookingDates] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, min_length=11, max_length=21)


class UpdateBookingResponseSchema(BaseModel):
    """
    Schema for response after updating a booking.
    """
    bookingid: int
    booking: BookingSchema


class UnavailableDatesQuerySchema(BaseModel):
    """
    Schema for query parameters to check room availability in date range.
    """
    checkin: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$", description="Check-in date (YYYY-MM-DD)")
    checkout: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$", description="Check-out date (YYYY-MM-DD)")

    @field_validator("checkout")
    @classmethod
    def validate_checkout(cls, v: str, info) -> str:
        checkin = info.data.get("checkin")
        if not checkin:
            return v
        try:
            checkin_date = date.fromisoformat(checkin)
            checkout_date = date.fromisoformat(v)
        except ValueError:
            raise ValueError("Invalid date format")
        validate_date_range(checkin_date, checkout_date)
        return v


class UnavailableRoom(BaseModel):
    """
    Schema for a single unavailable room in response.
    """
    roomid: int = Field(..., ge=1, description="ID of unavailable room (positive integer)")


class UnavailableDatesResponseSchema(RootModel[List[UnavailableRoom]]):
    """
    Schema for response listing unavailable rooms in a date range.
    Returns an array of room IDs. Empty array means all rooms are available.
    """
    model_config = ConfigDict(
        json_schema_extra={
            "example": [
                {"roomid": 1},
                {"roomid": 2}
            ]
        }
    )


class GetSummaryQuerySchema(BaseModel):
    """
    Schema for query parameters to get booking summary by room ID.
    Accepts stringified integer (e.g. ?roomid=1).
    This matches API contract: roomid is passed as string in query params.
    """
    roomid: str

    @field_validator("roomid")
    @classmethod
    def validate_roomid(cls, v: str) -> str:
        return validate_stringified_positive_int(v)


class SummaryBookingItem(BaseModel):
    """
    Schema for an item in booking summary — contains only booking dates.
    """
    model_config = ConfigDict(populate_by_name=True)

    booking_dates: BookingDates = Field(alias="bookingDates")


class GetSummaryResponseSchema(BaseModel):
    """
    Schema for response from /booking/summary — list of booking date ranges.
    May be empty.
    """
    bookings: List[SummaryBookingItem]


class DeleteBookingRequestSchema(BaseModel):
    """
    Schema for DELETE /{id} — validates booking ID.
    """
    id: int = Field(..., ge=1, description="Booking ID to delete, positive integer")