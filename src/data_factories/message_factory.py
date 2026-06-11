from utils.fakers import fake
from clients.message.message_schema import CreateMessageRequestSchema


class MessageRequestFactory:
    """
    Factory for creating valid message requests.
    """

    @classmethod
    def build(cls, **overrides) -> CreateMessageRequestSchema:
        """
        Creates a valid CreateMessageRequestSchema object with all required fields filled.

        Args:
            **overrides: Fields to override, e.g., name="John", subject="Issue".

        Returns:
            Ready-to-use schema object for POST /message.
        """
        base_data = {
            "name": fake.first_name(),
            "email": fake.email(),
            "phone": fake.phone(),
            "subject": fake.message_subject(),
            "description": fake.message_description(),
        }

        base_data.update(overrides)

        return CreateMessageRequestSchema(**base_data)
