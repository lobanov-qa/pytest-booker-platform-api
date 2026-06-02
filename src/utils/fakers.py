from faker import Faker

from datetime import date, timedelta
from typing import Optional


class Fake:
    """
    Generates random test data using the Faker library.
    All methods are wrapped to provide deterministic, valid test data
    matching the API constraints (length limits, patterns, etc.).
    """

    def __init__(self, faker: Faker):
        self.faker = faker

    def integer(self, start: int = 1, end: int = 100) -> int:
        """Generates a random integer in [start, end]."""
        return self.faker.random_int(start, end)

    def booking_dates(
        self,
        checkin: Optional[date] = None,
        delta: int = 1,
        max_days_ahead: int = 90
    ) -> dict:
        """Generates valid booking dates with checkin < checkout."""
        if checkin is None:
            random_offset = self.faker.random_int(min=1, max=max_days_ahead)
            checkin = date.today() + timedelta(days=random_offset)
        delta = max(delta, 1)
        checkout = checkin + timedelta(days=delta)
        return {"checkin": checkin.isoformat(), "checkout": checkout.isoformat()}

    def room_id(self) -> int:
        """Generates a valid room ID (integer >= 1)."""
        return self.integer(1, 100)

    def phone(self) -> str:
        """Generates a phone number (11-21 chars, digits only)."""
        phone_number = self.faker.phone_number()
        while len(phone_number) < 11:
            phone_number = self.faker.phone_number()
        return phone_number[:21]

    def first_name(self, min_length: int = 3, max_length: int = 18) -> str:
        """Generates a first name within length constraints."""
        name = self.faker.first_name()
        while len(name) < min_length or len(name) > max_length:
            name = self.faker.first_name()
        return name

    def last_name(self, min_length: int = 3, max_length=30) -> str:
        """Generates a last name within length constraints."""
        name = self.faker.last_name()
        while len(name) < min_length or len(name) > max_length:
            name = self.faker.last_name()
        return name

    def deposit_paid(self) -> bool:
        return self.faker.boolean()

    def email(self, domain: str | None = "example.com") -> str:
        return self.faker.email(domain=domain)

    def room_name(self) -> str:
        return f"Room {self.faker.word().title()} {self.integer(1, 999)}"

    def room_type(self) -> str:
        return self.faker.random_element(["Single", "Double", "Twin", "Family", "Suite"])

    def room_accessible(self) -> bool:
        return self.faker.boolean()

    def room_image(self) -> str:
        return f"https://dummyimage.com/{self.integer(100, 800)}x{self.integer(50, 600)}"

    def room_description(self) -> str:
        return self.faker.paragraph(nb_sentences=2)

    def room_features(self) -> list[str]:
        return self.faker.words(nb=3)

    def room_price(self) -> int:
        return self.integer(50, 999)

    def message_subject(self) -> str:
        return self.faker.sentence(nb_words=4)[:100]

    def message_description(self) -> str:
        return self.faker.paragraph(nb_sentences=4)[:2000]

    def company_name(self) -> str:
        return self.faker.company()

    def branding_description(self) -> str:
        return self.faker.catch_phrase()

    def directions_text(self) -> str:
        return self.faker.paragraph(nb_sentences=2)

    def logo_url(self) -> str:
        return f"https://placekitten.com/{self.integer(200, 800)}/{self.integer(200, 600)}"

    def map_latitude(self) -> float:
        return self.faker.latitude()

    def map_longitude(self) -> float:
        return self.faker.longitude()

    def address_line1(self) -> str:
        return self.faker.street_address()

    def address_line2(self) -> str:
        return self.faker.secondary_address()

    def post_town(self) -> str:
        return self.faker.city()

    def county(self) -> str:
        return self.faker.state()

    def post_code(self) -> str:
        return self.faker.postcode()


fake = Fake(faker=Faker())
