import allure

from clients.message.message_schema import CreateMessageRequestSchema, MessageSchema
from utils.assertions.base import assert_equal, assert_is_instance, assert_positive
from utils.logger import get_logger

logger = get_logger("MESSAGE_ASSERTIONS")


@allure.step("Check create message response")
def assert_create_message_response(request: CreateMessageRequestSchema, response: MessageSchema):
    """
    Verifies that the message creation response matches the request.

    :param request: Initial request to create a message.
    :param response: API response with message data.
    :raises AssertionError: If at least one field does not match.
    """
    logger.info("Check create message response")
    assert_positive(response.messageid, "messageid not positive")
    assert_equal(response.name, request.name, "name")
    assert_equal(response.email, request.email, "email")
    assert_equal(response.phone, request.phone, "phone")
    assert_equal(response.subject, request.subject, "subject")
    assert_equal(response.description, request.description, "description")


@allure.step("Check message")
def assert_message(actual: MessageSchema, expected: MessageSchema):
    """
    Checks that the actual message data matches the expected one.

    :param actual: Actual message data.
    :param expected: Expected message data.
    :raises AssertionError: If at least one field does not match.
    """
    logger.info("Check message")
    assert_equal(actual.messageid, expected.messageid, "messageid")
    assert_equal(actual.name, expected.name, "name")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.phone, expected.phone, "phone")
    assert_equal(actual.subject, expected.subject, "subject")
    assert_equal(actual.description, expected.description, "description")


@allure.step("Check get message response")
def assert_get_message_response(
    get_response: MessageSchema,
    create_response: MessageSchema
):
    """
    Checks that the response when receiving a message matches the response when creating it.

    :param get_response: API response when requesting message data.
    :param create_response: Message data from creation response.
    :raises AssertionError: If message data does not match.
    """
    logger.info("Check get message response")
    assert_message(get_response, create_response)


@allure.step("Check messages list contains message")
def assert_messages_list_contains(messages: list, expected_message: MessageSchema):
    """
    Checks that the list of message summaries contains the expected message.

    The list from GET /message/ returns MessageSummarySchema objects (with `id`),
    while expected_message is a full MessageSchema (with `messageid`).
    Comparison is done on overlapping fields: name, subject.

    :param messages: List of message summaries from API response.
    :param expected_message: Expected full message data from creation response.
    :raises AssertionError: If the message is not found or data does not match.
    """
    logger.info("Check messages list contains message")
    assert_is_instance(messages, list, "messages")

    found_message = None
    for message in messages:
        if message.name == expected_message.name and message.subject == expected_message.subject:
            found_message = message
            break

    assert found_message is not None, (
        f"Expected message with name '{expected_message.name}' not found in response. "
        f"Found names: {[m.name for m in messages]}"
    )


