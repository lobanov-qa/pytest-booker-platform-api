from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.auth.auth_client import AuthClient
from clients.auth.auth_schema import LoginRequestSchema, ValidateRequestSchema, LogoutRequestSchema
from clients.auth.routes import AuthRoutes
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import (
    assert_status_code,
    assert_is_instance,
    assert_is_true,
    assert_equal,
    assert_not_none
)


@pytest.mark.regression
@pytest.mark.authentication
@allure.epic(AllureEpic.AUTH)
@allure.feature(AllureFeature.AUTH_LOGIN)
class TestAuthentication:
    """
    Test suite for authentication operations.
    Covers login, token validation, and logout functionality.
    """

    @allure.story(AllureStory.LOGIN_WITH_VALID_CREDENTIALS)
    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.AUTH, AllureTag.CREATE_ENTITY)
    @allure.title("POST /auth/login - Raw API method returns 200 with token cookie")
    def test_login_api_returns_token_in_cookies(self, authentication_client: AuthClient):
        """
        Positive test: Raw API login method.
        Validates status code and token presence in cookies.
        """
        request = LoginRequestSchema()
        response = authentication_client.login_api(request)
        
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_not_none(response.cookies.get("token"), "token cookie")

    @allure.story(AllureStory.LOGIN_WITH_VALID_CREDENTIALS)
    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.AUTH, AllureTag.CREATE_ENTITY)
    @allure.title("POST /auth/login - High-level method returns valid token")
    def test_login_returns_token(self, authentication_client: AuthClient):
        """
        Positive test: High-level login method.
        Returns parsed token string.
        """
        request = LoginRequestSchema()
        token = authentication_client.login(request)
        
        assert_is_instance(token, str, "token")
        assert_not_none(token, "token")
        assert_is_true(len(token) > 0, "token length")

    @allure.story(AllureStory.TOKEN_VALIDATION)
    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY)
    @allure.title("POST /auth/validate - Raw API method for valid token returns 200")
    def test_validate_api_returns_200_for_valid_token(self, authentication_client: AuthClient):
        """
        Positive test: Raw API validate method with valid token.
        Validates status code 200.
        """
        token = authentication_client.login(LoginRequestSchema())
        request = ValidateRequestSchema(token=token)
        
        response = authentication_client.validate_api(request)
        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.story(AllureStory.TOKEN_VALIDATION)
    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY)
    @allure.title("POST /auth/validate - High-level method returns True for valid token")
    def test_is_token_valid_returns_true_for_valid_token(self, authentication_client: AuthClient):
        """
        Positive test: High-level validate method.
        Returns True for valid token.
        """
        token = authentication_client.login(LoginRequestSchema())
        is_valid = authentication_client.is_token_valid(token)
        
        assert_is_true(is_valid, "token validity")

    @allure.story(AllureStory.TOKEN_VALIDATION)
    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("POST /auth/validate - High-level method returns False for invalid token")
    def test_is_token_valid_returns_false_for_invalid_token(self, authentication_client: AuthClient):
        """
        Negative test: High-level validate method.
        Returns False for invalid token.
        """
        is_valid = authentication_client.is_token_valid("invalid_token")
        assert_equal(is_valid, False, "token validity")

    @allure.story(AllureStory.TOKEN_VALIDATION)
    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("POST /auth/validate - High-level method returns False for empty/null token")
    def test_is_token_valid_returns_false_for_empty_token(self, authentication_client: AuthClient):
        """
        Negative test: High-level validate method.
        Returns False for empty/null token.
        """
        is_valid_empty = authentication_client.is_token_valid("")
        assert_equal(is_valid_empty, False, "empty token validity")
        
        is_valid_none = authentication_client.is_token_valid(None)
        assert_equal(is_valid_none, False, "null token validity")

    @allure.story(AllureStory.USER_LOGOUT)
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY)
    @allure.title("POST /auth/logout - Raw API method returns 200 for valid token")
    def test_logout_api_returns_200_for_valid_token(self, authentication_client: AuthClient):
        """
        Positive test: Raw API logout method.
        Validates status code 200.
        """
        token = authentication_client.login(LoginRequestSchema())
        request = LogoutRequestSchema(token=token)
        
        response = authentication_client.logout_api(request)
        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.story(AllureStory.USER_LOGOUT)
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY)
    @allure.title("POST /auth/logout - High-level method returns True for valid token")
    def test_logout_returns_true_on_success(self, authentication_client: AuthClient):
        """
        Positive test: High-level logout method.
        Returns True for successful logout.
        """
        token = authentication_client.login(LoginRequestSchema())
        logout_result = authentication_client.logout(token)
        
        assert_is_true(logout_result, "logout success")


    @allure.story(AllureStory.USER_LOGOUT)
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.AUTH, AllureTag.NEGATIVE)
    @allure.title("POST /auth/logout - High-level method returns False for second logout")
    def test_logout_after_logout_returns_false(self, authentication_client: AuthClient):
        """
        Negative test: High-level logout method for already logged out token.
        Returns False for second logout attempt.
        """
        token = authentication_client.login(LoginRequestSchema())
        
        # First logout should succeed
        first_logout = authentication_client.logout(token)
        assert_is_true(first_logout, "first logout")
        
        # Second logout should fail
        second_logout = authentication_client.logout(token)
        assert_equal(second_logout, False, "second logout")

    @allure.story(AllureStory.TOKEN_VALIDATION)
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY)
    @allure.title("POST /auth/validate - High-level method returns False after logout")
    def test_token_is_invalid_after_logout(self, authentication_client: AuthClient):
        """
        Positive test: High-level validate method after logout.
        Returns False for invalidated token.
        """
        token = authentication_client.login(LoginRequestSchema())
        
        # Logout should succeed
        logout_result = authentication_client.logout(token)
        assert_is_true(logout_result, "logout")
        
        # Token should be invalid after logout
        is_valid = authentication_client.is_token_valid(token)
        assert_equal(is_valid, False, "token validity after logout")

    @allure.story(AllureStory.USER_LOGOUT)
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("POST /auth/logout - High-level method returns False for invalid token")
    def test_logout_returns_false_on_invalid_token(self, authentication_client: AuthClient):
        """
        Negative test: High-level logout method with invalid token.
        Returns False for invalid token.
        """
        logout_result = authentication_client.logout("invalid_token")
        assert_equal(logout_result, False, "logout with invalid token")
