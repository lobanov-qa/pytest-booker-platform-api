from enum import StrEnum


class AllureFeature(StrEnum):
    AUTH_LOGIN = "User Authentication"
    AUTH_TOKEN = "Token Management"

    BOOKING_CRUD = "Booking Management (CRUD)"
    BOOKING_VALIDATION = "Booking Validation & Availability"

    ROOM_CRUD = "Room Management (CRUD)"
    ROOM_AVAILABILITY = "Room Availability"

    MESSAGE_CRUD = "Messaging (CRUD)"
    MESSAGE_STATUS = "Message Read Status"

    BRANDING_CONFIG = "Branding Configuration"
    REPORT_GENERATION = "Report Generation"

    CHECK_HEALTH = "Check Health"