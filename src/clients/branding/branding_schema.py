from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional


class AddressSchema(BaseModel):
    """
    Schema for address information (nested in Branding).
    All fields are required.
    """
    model_config = ConfigDict(populate_by_name=True)

    line1: str = Field(..., min_length=1, description="Address line 1")
    line2: str = Field(..., min_length=1, description="Address line 2")
    post_town: str = Field(..., alias="postTown", min_length=1, description="Post town")
    county: str = Field(..., min_length=1, description="County")
    post_code: str = Field(..., alias="postCode", min_length=1, description="Post code")


class MapSchema(BaseModel):
    """
    Schema for map coordinates (nested in Branding).
    Both latitude and longitude are required.
    """
    latitude: float = Field(..., description="Latitude coordinate")
    longitude: float = Field(..., description="Longitude coordinate")


class ContactSchema(BaseModel):
    """
    Schema for contact information (nested in Branding).
    All fields are required.
    """
    name: str = Field(
        ...,
        min_length=3,
        max_length=40,
        pattern=r"[A-Za-z& ]*",
        description="Contact person name, 3-40 chars, letters/&/space only"
    )
    phone: str = Field(..., min_length=1, description="Contact phone number")
    email: EmailStr = Field(..., min_length=1, description="Contact email address")


class BrandingSchema(BaseModel):
    """
    Schema for branding information (GET / response).
    Required fields: description, directions, logo_url, name.
    """
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        pattern=r"[A-Za-z& ]*",
        description="Brand/organization name, 3-100 chars"
    )
    map: Optional[MapSchema] = Field(None, description="Map coordinates")
    logo_url: str = Field(..., alias="logoUrl", min_length=1, description="Logo image URL")
    description: str = Field(
        ...,
        min_length=3,
        max_length=500,
        pattern=r"[a-zA-Z,&. ]*",
        description="Brand description, 3-500 chars"
    )
    directions: str = Field(..., min_length=1, description="Directions to the venue")
    contact: Optional[ContactSchema] = Field(None, description="Contact information")
    address: Optional[AddressSchema] = Field(None, description="Physical address")

