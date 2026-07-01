from datetime import datetime, timedelta
from utils.fakers import fake
from clients.report.report_schema import EntrySchema


class EntryFactory:
    """
    Factory for creating valid report entries.
    """

    @classmethod
    def build(cls, **overrides) -> EntrySchema:
        """
        Creates a valid EntrySchema object with all required fields filled.

        Args:
            **overrides: Fields to override, e.g., title="Custom Title".

        Returns:
            Ready-to-use schema object.
        """
        start = datetime.now() + timedelta(days=fake.integer(1, 30))
        end = start + timedelta(days=fake.integer(1, 7))

        base_data = {
            "start": start,
            "end": end,
            "title": f"{fake.first_name()} {fake.last_name()} - Room: {fake.room_id()}",
        }

        base_data.update(overrides)

        return EntrySchema(**base_data)