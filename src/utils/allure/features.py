from enum import StrEnum


class AllureFeature(StrEnum):
    """Allure feature labels for test grouping."""

    AUTH_LOGIN = "User Authentication"
    AUTH_TOKEN = "Token Management"  # noqa: S105  # Allure label, not a credential

    BOOKING_CRUD = "Booking Management (CRUD)"
    BOOKING_VALIDATION = "Booking Validation & Availability"

    ROOM_CRUD = "Room Management (CRUD)"
    ROOM_AVAILABILITY = "Room Availability"

    MESSAGE_CRUD = "Messaging (CRUD)"
    MESSAGE_STATUS = "Message Read Status"

    BRANDING_CONFIG = "Branding Configuration"
    REPORT_GENERATION = "Report Generation"

    CHECK_HEALTH = "Check Health"

    FULL_AUDIT_TRAIL = "Full Audit Trail"
