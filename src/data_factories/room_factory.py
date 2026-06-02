from utils.fakers import fake
from clients.room.room_schema import RoomRequestSchema


class RoomRequestFactory:
    """
    Factory for creating valid room requests.
    """

    @classmethod
    def build(cls, **overrides) -> RoomRequestSchema:
        """
        Creates a valid RoomRequestSchema object with all optional fields filled.

        Args:
            **overrides: Fields to override, e.g., room_name="Suite 101".

        Returns:
            Ready-to-use schema object for POST /room or PUT /room/{id}.
        """
        base_data = {
            "room_name": fake.room_name(),
            "room_type": fake.room_type(),
            "accessible": fake.room_accessible(),
            "image": fake.room_image(),
            "description": fake.room_description(),
            "features": fake.room_features(),
            "room_price": fake.room_price(),
        }

        base_data.update(overrides)

        return RoomRequestSchema(**base_data)