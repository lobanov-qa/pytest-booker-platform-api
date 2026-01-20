from datetime import date


def validate_date_range(checkin: date, checkout: date) -> None:
    """
    Validates that checkout date is after check-in date.
    Raises ValueError if not.

    Used across multiple schemas to avoid duplication.
    Ensures business rule: "You cannot check out before or on check-in day".
    """
    if not isinstance(checkin, date) or not isinstance(checkout, date):
        raise ValueError("Both checkin and checkout must be date objects")
    if checkout <= checkin:
        raise ValueError("Checkout must be after check-in date")


def validate_stringified_positive_int(v: str) -> str:
    """
    Validates that a string is a positive integer (e.g. '1', '123').
    Used for query parameters like roomid, bookingid, etc.

    Raises:
        ValueError: If string is not a digit or <= 0
    """
    if not v.isdigit():
        raise ValueError("Must be a stringified integer (e.g. '123')")
    if int(v) < 1:
        raise ValueError("Must represent a positive integer")
    return v