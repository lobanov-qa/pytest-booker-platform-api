import re

from utils.fakers import fake
from clients.branding.branding_schema import (
    BrandingSchema,
    MapSchema,
    ContactSchema,
    AddressSchema
)


def _clean_name(value: str) -> str:
    """Remove characters not allowed in name fields: only letters, & and spaces."""
    return re.sub(r"[^A-Za-z& ]", "", value).strip()


def _clean_description(value: str) -> str:
    """Remove characters not allowed in description: letters, commas, &, dots, spaces."""
    return re.sub(r"[^a-zA-Z,&. ]", "", value).strip()


def _clean_phone(value: str) -> str:
    """Keep only digits and optional leading +, max 15 chars (DB column limit)."""
    cleaned = re.sub(r"[^\d+]", "", value)
    if cleaned.startswith("+"):
        cleaned = "+" + re.sub(r"\+", "", cleaned)
    else:
        cleaned = re.sub(r"\+", "", cleaned)
    return cleaned[:15]


class BrandingFactory:
    """
    Factory for creating valid Branding objects.
    Used for both GET comparison and PUT update requests.

    NOTE: logoUrl MUST be a full URL (e.g., http://...), not a relative path.
    The API rejects relative paths even though GET may return them.
    """

    @classmethod
    def build(cls, **overrides) -> BrandingSchema:
        """
        Creates a valid BrandingSchema with all required fields populated.

        :param overrides: Fields to override, e.g., name="New Name".
        :return: Ready-to-use schema for PUT /branding/.
        """
        base_data = {
            "name": _clean_name(fake.company_name()),
            "description": _clean_description(fake.branding_description()),
            "directions": fake.directions_text(),
            "logo_url": fake.logo_url(),
            "map": MapSchema(
                latitude=fake.map_latitude(),
                longitude=fake.map_longitude()
            ),
            "contact": ContactSchema(
                name=_clean_name(fake.company_name()),
                phone=_clean_phone(fake.phone()),
                email=fake.email()
            ),
            "address": AddressSchema(
                line1=fake.address_line1(),
                line2=fake.address_line2(),
                post_town=fake.post_town(),
                county=fake.county(),
                post_code=fake.post_code()
            ),
        }

        base_data.update(overrides)

        return BrandingSchema(**base_data)
