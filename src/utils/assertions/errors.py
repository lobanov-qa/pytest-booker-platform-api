from typing import Optional, List

import allure

from clients.errors_schema import ValidationErrorSchema, BaseErrorResponse
from utils.assertions.base import assert_equal
from utils.logger import get_logger

logger = get_logger("ERRORS_ASSERTIONS")


@allure.step("Check validation error")
def assert_validation_error(
    error: ValidationErrorSchema,
    expected_status: int = 400,
    expected_error: str = "BAD_REQUEST",
    expected_fields: Optional[List[str]] = None
) -> None:
    """
    Validates key aspects of a validation error response.
    Does not require exact text match - only checks for field presence.

    :param error: Error received from the API.
    :param expected_status: Expected HTTP status code (default: 400).
    :param expected_error: Expected error type (default: "BAD_REQUEST").
    :param expected_fields: List of field names that should be mentioned in error messages.
    :raises AssertionError: If any validation fails.
    """
    logger.info(f"Validating error: {error.error}")

    # 1. Validate status and error type
    assert_equal(error.error_code, expected_status, "error_code")
    assert_equal(error.error, expected_error, "error_type")

    # 2. Validate that specified fields are present in error messages
    if expected_fields:
        error_text = " ".join(error.field_errors).lower()
        for field in expected_fields:
            assert field.lower() in error_text, (
                f"Expected field '{field}' not found in error messages: {error.field_errors}"
            )


@allure.step("Check base error response")
def assert_base_error_response(
    error: BaseErrorResponse,
    expected_status: int = 400,
    path_contains: Optional[str] = None
) -> None:
    """
    Validates a standard Spring Boot error response (e.g., for missing query parameters).

    :param error: Error response received from the API.
    :param expected_status: Expected HTTP status code.
    :param path_contains: Substring that should be present in the path.
    :raises AssertionError: If any validation fails.
    """
    logger.info(f"Validating query error: {error.error}")

    assert_equal(error.status, expected_status, "error_status")

    if path_contains:
        assert path_contains in error.path, (
            f"Expected '{path_contains}' in path, got '{error.path}'"
        )
