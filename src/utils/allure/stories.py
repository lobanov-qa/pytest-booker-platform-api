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