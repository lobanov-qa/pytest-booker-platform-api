from enum import StrEnum


class AllureEpic(StrEnum):
    """Allure epic labels for test grouping."""

    AUTH = "Authentication"
    BOOKING = "Booking"
    ROOM = "Room"
    MESSAGE = "Messaging"
    BRANDING = "Branding"
    REPORT = "Reporting"
    HEALTH = "API Health"

    E2E = "End-to-End"
