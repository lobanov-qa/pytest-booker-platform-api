from typing import Any, Sized, List

import allure

from utils.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")


@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Checks that the actual response status code matches the expected one.

    :param actual: Actual response status code.
    :param expected: Expected status code.
    :raises AssertionError: If the status codes do not match.
    """
    logger.info(f"Check that response status code equals to {expected}")

    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )

@allure.step("Check that {name} equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Checks that the actual value is equal to the expected value.

    :param name: Name of the value being checked.
    :param actual: Actual value.
    :param expected: Expected value.
    :raises AssertionError: If the actual value is not equal to the expected value.
    """
    logger.info(f'Check that "{name}" equals to {expected}')

    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}'
    )

@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str):
    """
    Checks that the actual value is true.

    :param name: Name of the value being checked.
    :param actual: Actual value.
    :raises AssertionError: If the actual value is false.
    """
    logger.info(f'Check that "{name}" is true')

    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Checks that the lengths of two objects are the same.

    :param name: The name of the object being checked.
    :param actual: Actual object.
    :param expected: The expected object.
    :raises AssertionError: If the lengths do not match.
    """
    with allure.step(f"Check that length of {name} equals to {len(expected)}"):
        logger.info(f'Check that length of "{name}" equals to {len(expected)}')

        assert len(actual) == len(expected), (
            f'Incorrect object length: "{name}". '
            f'Expected length: {len(expected)}. '
            f'Actual length: {len(actual)}'
        )



@allure.step("Check that {name} is greater than zero")
def assert_positive(actual: int, name: str):
    """Checks that the value is positive (greater than zero)."""
    logger.info(f'Check that "{name}" is greater than zero: {actual}')
    assert actual > 0, f'Expected "{name}" > 0, but got: {actual}'


def assert_is_instance(obj: Any, expected_type: type, name: str):
    """Checks that an object is an instance of the specified type."""
    expected_type_name = expected_type.__name__
    actual_type_name = type(obj).__name__

    with allure.step(f'Check that "{name}" is instance of {expected_type_name}'):
        logger.info(f'Check that "{name}" is instance of {expected_type_name} (actual: {actual_type_name})')
        assert isinstance(obj, expected_type), (
            f'Expected "{name}" to be instance of {expected_type_name}, '
            f'but got {actual_type_name}'
        )




@allure.step("Check that {item} is in {collection_name}")
def assert_in(item: Any, collection: List[Any], collection_name: str):
    """Checks that an element is present in the collection."""
    logger.info(f'Check that "{item}" is in "{collection_name}"')
    assert item in collection, (
        f'Expected "{item}" to be in "{collection_name}", but it is not. '
        f'Available: {collection}'
    )


@allure.step("Check that length of {name} is {expected_length}")
def assert_length_equal(actual: Sized, expected_length: int, name: str):
    """Checks that the length of an object is equal to the expected length."""
    logger.info(f'Check that length of "{name}" equals to {expected_length}')
    actual_length = len(actual)
    assert actual_length == expected_length, (
        f'Expected length of "{name}" to be {expected_length}, but got {actual_length}'
    )


@allure.step("Check that {name} is not None")
def assert_not_none(actual: Any, name: str):
    """Checks that the value is not None."""
    logger.info(f'Check that "{name}" is not None')
    assert actual is not None, f'Expected "{name}" to be not None, but it is None'