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
    Проверяет ключевые аспекты ошибки валидации.
    Не требует точного совпадения текста — только наличие полей.

    :param error: Ошибка, полученная от API.
    :param expected_status: Ожидаемый HTTP статус (по умолчанию 400).
    :param expected_error: Ожидаемый тип ошибки (по умолчанию BAD_REQUEST).
    :param expected_fields: Список полей, которые должны быть упомянуты в ошибках.
    """
    logger.info(f"Validating error: {error.error}")

    # 1. Проверяем статус и тип
    assert_equal(error.error_code, expected_status, "error_code")
    assert_equal(error.error, expected_error, "error_type")

    # 2. Проверяем, что указанные поля есть в ошибках
    if expected_fields:
        error_text = " ".join(error.field_errors).lower()
        for field in expected_fields:
            assert field.lower() in error_text, (
                f"Expected field '{field}' not found in error messages: {error.field_errors}"
            )


@allure.step("Check query validation error")
def assert_base_error_response(
    error: BaseErrorResponse,
    expected_status: int = 400,
    path_contains: Optional[str] = None
) -> None:
    """
    Проверяет стандартную ошибку Spring Boot (например, при отсутствии query-параметров).

    :param error: Ошибка, полученная от API.
    :param expected_status: Ожидаемый HTTP статус.
    :param path_contains: Подстрока, которая должна быть в пути.
    """
    logger.info(f"Validating query error: {error.error}")

    assert_equal(error.status, expected_status, "error_status")

    if path_contains:
        assert path_contains in error.path, (
            f"Expected '{path_contains}' in path, got '{error.path}'"
        )
