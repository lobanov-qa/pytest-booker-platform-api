from enum import StrEnum

class AllureStory(StrEnum):
    # Authentication Stories
    LOGIN_WITH_VALID_CREDENTIALS = "User login to the system"
    USER_LOGOUT = "User logout from the system"
    TOKEN_VALIDATION = "Token validation process"

    # Booking Stories - Public endpoints
    BOOKING_CREATION = "Create new booking"
    BOOKING_VALIDATION = "Validate booking data"
    AVAILABILITY_CHECK = "Check room availability"
    BOOKING_SUMMARY = "Get booking summary"

    # Booking Stories - Private endpoints (authenticated)
    BOOKING_RETRIEVAL = "Retrieve booking details"
    BOOKING_FILTERING = "Filter bookings by criteria"
    BOOKING_UPDATE = "Update existing booking"
    BOOKING_DELETION = "Delete booking"
    BOOKING_LIST = "List all bookings"

    # Room Stories
    ROOM_LIST = "List all rooms"
    ROOM_CREATION = "Create new room"
    ROOM_RETRIEVAL = "Retrieve room details"
    ROOM_UPDATE = "Update existing room"
    ROOM_DELETION = "Delete room"

    # Message Stories
    MESSAGE_CREATION = "Create new message"
    MESSAGE_LIST = "List all messages"
    MESSAGE_RETRIEVAL = "Retrieve message details"
    MESSAGE_READ = "Mark message as read"
    MESSAGE_DELETION = "Delete message"

    # Branding Stories
    BRANDING_GET = "Get branding data"
    BRANDING_UPDATE = "Update branding"

    # Report Stories
    REPORT_GENERATION = "Generate report for all rooms"
    ROOM_REPORT = "Generate report for specific room"
    REPORT_BY_ROOM = "Generate report for specific room"
    REPORT_ALL = "Get all reports"

    # E2E Stories
    FULL_HOTEL_AUDIT = "Complete hotel audit"
    ROOM_CREATION_IN_FLOW = "Create room and verify in public list"
    BOOKING_WITHIN_AUDIT = "Create booking and verify within audit flow"
    MESSAGE_WITHIN_AUDIT = "Create, read, and verify message"
    BOOKING_CANCELLATION = "Cancel booking and verify report"
