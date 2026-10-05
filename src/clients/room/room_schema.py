from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator

from utils.validators import validate_date_range


class RoomType(StrEnum):
    """Room types as defined in OpenAPI spec."""

    SINGLE = "Single"
    DOUBLE = "Double"
    TWIN = "Twin"
    FAMILY = "Family"
    SUITE = "Suite"


class RoomResponseSchema(BaseModel):
    """
    Schema for room response (GET /rooms/{id}, GET /rooms).
    All fields are required in responses.
    """

    model_config = ConfigDict(populate_by_name=True)

    roomid: int = Field(..., ge=1, description="Room ID, minimum 1")
    room_name: str = Field(..., alias="roomName", min_length=1)
    room_type: RoomType = Field(..., alias="type")
    accessible: bool
    image: str
    description: str
    features: list[str]
    room_price: int = Field(..., alias="roomPrice", ge=1, le=999)


class RoomRequestSchema(BaseModel):
    """
    Schema for creating and updating a room (POST /rooms, PUT /rooms/{id}).
    Only room_name and type are required per OpenAPI spec.
    """

    model_config = ConfigDict(populate_by_name=True)

    room_name: str = Field(..., alias="roomName", min_length=1)
    room_type: RoomType = Field(..., alias="type")
    accessible: bool | None = None
    image: str | None = None
    description: str | None = None
    features: list[str] | None = None
    room_price: int | None = Field(None, alias="roomPrice", ge=1, le=999)


class RoomsResponseSchema(BaseModel):
    """
    Schema for response containing a list of rooms (GET /rooms).
    """

    rooms: list[RoomResponseSchema]


class GetRoomsQuerySchema(BaseModel):
    """
    Schema for query parameters when getting rooms (GET /rooms).
    checkin and checkout are optional parameters for filtering availability.
    """

    checkin: str | None = Field(
        None, pattern=r"^\d{4}-\d{2}-\d{2}$", description="Check-in date (YYYY-MM-DD)"
    )
    checkout: str | None = Field(
        None, pattern=r"^\d{4}-\d{2}-\d{2}$", description="Check-out date (YYYY-MM-DD)"
    )

    @field_validator("checkout")
    @classmethod
    def validate_checkout(cls, v: str | None, info) -> str | None:
        if v is None:
            return v
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
