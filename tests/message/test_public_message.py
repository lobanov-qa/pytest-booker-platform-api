from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.message.public_message_client import PublicMessageClient
from clients.message.message_schema import (
    MessageSchema,
    MessagesResponseSchema,
    CountSchema,
)
from clients.message.routes import MessageRoutes
from clients.errors_schema import  ValidationErrorSchema
from utils.assertions.errors import  assert_validation_error
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import (
    assert_status_code,
    assert_positive,
    assert_is_instance,
    assert_not_none,
)
from utils.assertions.schema import validate_json_schema
from utils.assertions.message import (
    assert_create_message_response,
    assert_messages_list_contains,
)


@pytest.mark.message
@pytest.mark.regression
@allure.tag(AllureTag.MESSAGE)
@allure.epic(AllureEpic.MESSAGE)
@allure.feature(AllureFeature.MESSAGE_CRUD)
class TestPublicMessageAPI:
    """
    Test suite for public message operations (no authentication required).
    Covers create message, get all messages, get count.
    """
    @pytest.mark.smoke
    @allure.story(AllureStory.MESSAGE_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("POST /message/ - Create message successfully (201)")
    @allure.severity(Severity.BLOCKER)
    def test_create_message_returns_201(
        self, public_message_client: PublicMessageClient, valid_message_request
    ):
        """
        Positive test: Create a new message with valid data.
        Real API returns 201 Created.
        Validates response structure and JSON schema compliance.
        """
        response = public_message_client.create_message_api(valid_message_request)
        assert_status_code(response.status_code, HTTPStatus.CREATED)
        response_data = MessageSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_create_message_response(valid_message_request, response_data)

    @allure.story(AllureStory.MESSAGE_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("POST /message/ - High-level method for creating message")
    @allure.severity(Severity.NORMAL)
    def test_create_message_high_level(
        self, public_message_client: PublicMessageClient, valid_message_request
    ):
        """
        Positive test: Use convenience method create_message().
        Returns parsed Pydantic model MessageSchema.
        """
        response_data = public_message_client.create_message(valid_message_request)
        assert_is_instance(response_data, MessageSchema, "response_data")
        assert_create_message_response(valid_message_request, response_data)

    @pytest.mark.smoke
    @allure.story(AllureStory.MESSAGE_LIST)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /message/ - Get all messages successfully (200)")
    @allure.severity(Severity.BLOCKER)
    def test_get_messages_returns_200(self, public_message_client: PublicMessageClient):
        """
        Positive test: Retrieve all messages.
        Validates response structure and JSON schema compliance.
        """
        response = public_message_client.get_messages_api()
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = MessagesResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_is_instance(response_data.messages, list, "messages")

    @pytest.mark.smoke
    @allure.story(AllureStory.MESSAGE_LIST)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /message/ - High-level method for getting all messages")
    @allure.severity(Severity.NORMAL)
    def test_get_messages_high_level(self, public_message_client: PublicMessageClient):
        """
        Positive test: Use convenience method get_messages().
        Returns parsed Pydantic model MessagesResponseSchema.
        """
        response_data = public_message_client.get_messages()
        assert_is_instance(response_data, MessagesResponseSchema, "response_data")
        assert_is_instance(response_data.messages, list, "messages")
        for msg in response_data.messages:
            assert_positive(msg.id, "message id")

    @pytest.mark.smoke
    @allure.story(AllureStory.MESSAGE_LIST)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /message/count - Get message count successfully (200)")
    @allure.severity(Severity.CRITICAL)
    def test_get_count_returns_200(self, public_message_client: PublicMessageClient):
        """
        Positive test: Retrieve total message count.
        Validates response structure and JSON schema compliance.
        """
        response = public_message_client.get_count_api()
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = CountSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_not_none(response_data.count, "count")

    @allure.story(AllureStory.MESSAGE_LIST)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /message/count - High-level method for getting message count")
    @allure.severity(Severity.NORMAL)
    def test_get_count_high_level(self, public_message_client: PublicMessageClient):
        """
        Positive test: Use convenience method get_count().
        Returns parsed Pydantic model CountSchema.
        """
        response_data = public_message_client.get_count()
        assert_is_instance(response_data, CountSchema, "response_data")
        assert_not_none(response_data.count, "count")

    @pytest.mark.smoke
    @allure.story(AllureStory.MESSAGE_LIST)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /message/ - Verify created message appears in messages list")
    @allure.severity(Severity.NORMAL)
    def test_get_messages_contains_created_message(
        self,
        public_message_client: PublicMessageClient,
        created_message,
    ):
        """
        Positive test: Verify that a newly created message appears in the messages list.
        Uses assert_messages_list_contains for validation.
        """
        response_data = public_message_client.get_messages()
        assert_messages_list_contains(response_data.messages, created_message.response)

    @allure.story(AllureStory.MESSAGE_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("POST /message/ - Create message with invalid data (400)")
    @allure.severity(Severity.NORMAL)
    def test_create_message_invalid_data_400(
        self, public_message_client: PublicMessageClient
    ):
        """
        Negative test: Create message with missing required fields.
        Returns 400 with ValidationErrorSchema.
        Uses assert_validation_error for structured error validation.
        """
        response = public_message_client.client.post(
            MessageRoutes.ROOT, json={}
        )
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        error_data = ValidationErrorSchema.model_validate_json(response.text)
        assert_validation_error(error_data, expected_fields=["name", "email", "phone", "subject", "message"])

    @allure.story(AllureStory.MESSAGE_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("POST /message/ - Create message with empty body (400)")
    @allure.severity(Severity.NORMAL)
    def test_create_message_empty_body_400(
        self, public_message_client: PublicMessageClient
    ):
        """
        Negative test: Create message with empty JSON body.
        Should return 400 Bad Request.
        """
        response = public_message_client.client.post(MessageRoutes.ROOT, json={})
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)

    @allure.story(AllureStory.MESSAGE_CREATION)
    @allure.tag(AllureTag.CREATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("POST /message/ - Create message with empty string fields (400)")
    @allure.severity(Severity.NORMAL)
    def test_create_message_empty_strings_400(
        self, public_message_client: PublicMessageClient
    ):
        """
        Negative test: Create message with empty string values.
        Returns 400 with ValidationErrorSchema.
        Uses assert_validation_error for structured error validation.
        """
        response = public_message_client.client.post(
            MessageRoutes.ROOT,
            json={"name": "", "email": "", "phone": "", "subject": "", "description": ""},
        )
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        error_data = ValidationErrorSchema.model_validate_json(response.text)
        assert_validation_error(error_data, expected_fields=["name", "email", "phone", "subject", "message"])
