from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.message.private_message_client import PrivateMessageClient
from clients.message.message_schema import MessageSchema
from clients.errors_schema import BaseErrorResponse
from fixtures.message import MessageFixture
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import (
    assert_status_code,
    assert_is_instance,
)
from utils.assertions.message import (
    assert_get_message_response,
)
from utils.assertions.errors import assert_base_error_response
from utils.assertions.schema import validate_json_schema


@pytest.mark.message
@pytest.mark.regression
@allure.tag(AllureTag.MESSAGE)
@allure.epic(AllureEpic.MESSAGE)
@allure.feature(AllureFeature.MESSAGE_STATUS)
class TestPrivateMessageAPI:
    """
    Test suite for authenticated message operations.
    Covers get message by ID, mark as read, and delete.
    """
    @pytest.mark.smoke
    @allure.story(AllureStory.MESSAGE_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("GET /message/{id} - Get message by ID successfully (200)")
    @allure.severity(Severity.BLOCKER)
    def test_get_message_returns_200(
        self,
        private_message_client: PrivateMessageClient,
        created_message: MessageFixture,
    ):
        """
        Positive test: Retrieve a specific message by ID.
        Validates response structure and JSON schema compliance.
        """
        message_id = created_message.message_id
        allure.dynamic.title(f"GET /message/{message_id} - Get message by ID successfully (200)")
        response = private_message_client.get_message_api(message_id)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = MessageSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_get_message_response(response_data, created_message.response)

    @pytest.mark.smoke
    @allure.story(AllureStory.MESSAGE_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("GET /message/{id} - High-level method for getting message by ID")
    @allure.severity(Severity.NORMAL)
    def test_get_message_high_level(
        self,
        private_message_client: PrivateMessageClient,
        created_message: MessageFixture,
    ):
        """
        Positive test: Use convenience method get_message().
        Returns parsed Pydantic model MessageSchema.
        """
        message_id = created_message.message_id
        allure.dynamic.title(f"GET /message/{message_id} - High-level method for getting message by ID")
        response_data = private_message_client.get_message(message_id)
        assert_is_instance(response_data, MessageSchema, "response_data")
        assert_get_message_response(response_data, created_message.response)

    @pytest.mark.smoke
    @allure.story(AllureStory.MESSAGE_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("GET /message/{id} - Get message matches created message data")
    @allure.severity(Severity.CRITICAL)
    def test_get_message_matches_created(
        self,
        private_message_client: PrivateMessageClient,
        created_message: MessageFixture,
    ):
        """
        Positive test: Verify that GET /message/{id} returns data matching the created message.
        """
        message_id = created_message.message_id
        allure.dynamic.title(f"GET /message/{message_id} - Get message matches created message data")

        get_response_data = private_message_client.get_message(message_id)
        assert_get_message_response(get_response_data, created_message.response)

    @pytest.mark.smoke
    @allure.story(AllureStory.MESSAGE_READ)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("PUT /message/{id}/read - Mark message as read (202)")
    @allure.severity(Severity.CRITICAL)
    def test_mark_read_returns_202(
        self,
        private_message_client: PrivateMessageClient,
        created_message: MessageFixture,
    ):
        """
        Positive test: Mark a message as read.
        Real API returns 202 Accepted.
        """
        message_id = created_message.message_id
        allure.dynamic.title(f"PUT /message/{message_id}/read - Mark message as read (202)")
        response = private_message_client.mark_read_api(message_id)
        assert_status_code(response.status_code, HTTPStatus.ACCEPTED)

    @allure.story(AllureStory.MESSAGE_READ)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("PUT /message/{id}/read - High-level mark as read")
    @allure.severity(Severity.NORMAL)
    def test_mark_read_high_level(
        self,
        private_message_client: PrivateMessageClient,
        created_message: MessageFixture,
    ):
        """
        Positive test: Use convenience method mark_read().
        Does not raise on success (202 is 2xx).
        """
        message_id = created_message.message_id
        allure.dynamic.title(f"PUT /message/{message_id}/read - High-level mark as read")
        private_message_client.mark_read(message_id)

    @pytest.mark.smoke
    @allure.story(AllureStory.MESSAGE_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.title("DELETE /message/{id} - Delete message (202)")
    @allure.severity(Severity.BLOCKER)
    def test_delete_message_returns_202(
        self,
        private_message_client: PrivateMessageClient,
        created_message: MessageFixture,
    ):
        """
        Positive test: Delete a message by ID.
        Real API returns 202 Accepted.
        Verifies message returns 500 after deletion (API crashes for non-existent IDs).
        """
        message_id = created_message.message_id
        allure.dynamic.title(f"DELETE /message/{message_id} - Delete message (202)")
        response = private_message_client.delete_message_api(message_id)
        assert_status_code(response.status_code, HTTPStatus.ACCEPTED)

        # Verify message is gone — API returns 500 for deleted/non-existent messages
        get_response = private_message_client.get_message_api(message_id)
        assert_status_code(get_response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    @allure.story(AllureStory.MESSAGE_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.title("DELETE /message/{id} - High-level delete message")
    @allure.severity(Severity.NORMAL)
    def test_delete_message_high_level(
        self,
        private_message_client: PrivateMessageClient,
        created_message: MessageFixture,
    ):
        """
        Positive test: Use convenience method delete_message().
        Verifies message returns 500 after deletion.
        """
        message_id = created_message.message_id
        allure.dynamic.title(f"DELETE /message/{message_id} - High-level delete message")
        private_message_client.delete_message(message_id)

        # Verify message is gone — API returns 500 for deleted/non-existent messages
        get_response = private_message_client.get_message_api(message_id)
        assert_status_code(get_response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    @allure.story(AllureStory.MESSAGE_RETRIEVAL)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.NEGATIVE)
    @allure.title("GET /message/9999 - Retrieve non-existent message (500)")
    @allure.severity(Severity.NORMAL)
    def test_get_message_not_found_500(
        self, private_message_client: PrivateMessageClient
    ):
        """
        Negative test: Request message with non-existent ID.
        Real API returns 500 Internal Server Error for non-existent message IDs.
        """
        response = private_message_client.get_message_api(9999)
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        error_data = BaseErrorResponse.model_validate_json(response.text)
        assert_base_error_response(error_data, expected_status=500, path_contains="/")

    @allure.story(AllureStory.MESSAGE_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("DELETE /message/9999 - Delete non-existent message (404)")
    @allure.severity(Severity.NORMAL)
    def test_delete_message_not_found_404(
        self, private_message_client: PrivateMessageClient
    ):
        """
        Negative test: Delete message with non-existent ID.
        API returns 404 Not Found for non-existent message IDs.
        """
        response = private_message_client.delete_message_api(9999)
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)

    @allure.story(AllureStory.MESSAGE_READ)
    @allure.tag(AllureTag.UPDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("PUT /message/1/read - Unauthorized request (403)")
    @allure.severity(Severity.CRITICAL)
    def test_mark_read_unauthorized_403(
        self, private_message_client_invalid: PrivateMessageClient
    ):
        """
        Negative test: Mark message as read with invalid authentication cookies.
        Should return 403 Forbidden.
        """
        response = private_message_client_invalid.mark_read_api(1)
        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)

    @allure.story(AllureStory.MESSAGE_DELETION)
    @allure.tag(AllureTag.DELETE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("DELETE /message/1 - Unauthorized request (403)")
    @allure.severity(Severity.CRITICAL)
    def test_delete_message_unauthorized_403(
        self, private_message_client_invalid: PrivateMessageClient
    ):
        """
        Negative test: Delete message with invalid authentication cookies.
        Should return 403 Forbidden.
        """
        response = private_message_client_invalid.delete_message_api(1)
        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)
