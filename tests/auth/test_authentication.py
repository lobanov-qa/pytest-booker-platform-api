import allure
import pytest
from allure_commons.types import Severity

from clients.auth.auth_schema import LoginRequestSchema
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.authentication
@allure.epic(AllureEpic.AUTH)
class TestAuthentication:
    @allure.feature(AllureFeature.AUTH_LOGIN)
    @allure.story(AllureStory.LOGIN_WITH_VALID_CREDENTIALS)
    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.AUTH, AllureTag.CREATE_ENTITY)
    @allure.title("User logs in with valid credentials and receives token")
    def test_login_returns_token(self, authentication_client):
        request = LoginRequestSchema()
        token = authentication_client.login(request)
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0

    @allure.feature(AllureFeature.AUTH_TOKEN)
    @allure.story(AllureStory.TOKEN_VALIDATION)
    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY)
    @allure.title("Checking the response to see if the token is valid")
    def test_is_token_valid_returns_true_for_valid_token(self, authentication_client):
        token = authentication_client.login(LoginRequestSchema())
        assert authentication_client.is_token_valid(token) is True

    @allure.feature(AllureFeature.AUTH_TOKEN)
    @allure.story(AllureStory.TOKEN_VALIDATION)
    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY)
    @allure.title("Checking the response using an invalid token")
    def test_is_token_valid_returns_false_for_invalid_token(self, authentication_client):
        assert authentication_client.is_token_valid("invalid_token") is False

    @allure.feature(AllureFeature.AUTH_TOKEN)
    @allure.story(AllureStory.TOKEN_VALIDATION)
    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY)
    @allure.title("Checking the response on the missing token")
    def test_is_token_valid_returns_false_for_empty_token(self, authentication_client):
        assert authentication_client.is_token_valid("") is False
        assert authentication_client.is_token_valid(None) is False

    @allure.feature(AllureFeature.AUTH_TOKEN)
    @allure.story(AllureStory.USER_LOGOUT)
    @allure.severity(Severity.NORMAL)
    @allure.title("Checking the logout")
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY)
    def test_logout_returns_true_on_success(self, authentication_client):
        token = authentication_client.login(LoginRequestSchema())
        assert authentication_client.logout(token) is True

    @allure.feature(AllureFeature.AUTH_TOKEN)
    @allure.story(AllureStory.USER_LOGOUT)
    @allure.severity(Severity.NORMAL)
    @allure.title("Checking logout after logout")
    @allure.tag(AllureTag.AUTH)
    def test_logout_after_logout_returns_false(self, authentication_client):
        token = authentication_client.login(LoginRequestSchema())
        authentication_client.logout(token)
        assert authentication_client.logout(token) is False


    @allure.feature(AllureFeature.AUTH_TOKEN)
    @allure.story(AllureStory.USER_LOGOUT)
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY)
    @allure.title("Checking that the token is not valid after logging out")
    def test_token_is_invalid_after_logout(self, authentication_client):
        token = authentication_client.login(LoginRequestSchema())
        authentication_client.logout(token)
        assert authentication_client.is_token_valid(token) is False




    @allure.feature(AllureFeature.AUTH_TOKEN)
    @allure.story(AllureStory.USER_LOGOUT)
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.AUTH, AllureTag.VALIDATE_ENTITY)
    @allure.title("Checking the logout on an invalid token")
    def test_logout_returns_false_on_invalid_token(self, authentication_client):
        assert authentication_client.logout("invalid") is False



