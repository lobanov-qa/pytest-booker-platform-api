import pytest

from clients.auth.auth_schema import LoginRequestSchema


@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:

    def test_login_returns_token(self, authentication_client):
        request = LoginRequestSchema()
        token = authentication_client.login(request)
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0

    def test_is_token_valid_returns_true_for_valid_token(self, authentication_client):
        token = authentication_client.login(LoginRequestSchema())
        assert authentication_client.is_token_valid(token) is True

    def test_is_token_valid_returns_false_for_invalid_token(self, authentication_client):
        assert authentication_client.is_token_valid("invalid_token") is False

    def test_is_token_valid_returns_false_for_empty_token(self, authentication_client):
        assert authentication_client.is_token_valid("") is False
        assert authentication_client.is_token_valid(None) is False

    def test_logout_returns_true_on_success(self, authentication_client):
        token = authentication_client.login(LoginRequestSchema())
        assert authentication_client.logout(token) is True

    def test_logout_returns_false_on_invalid_token(self, authentication_client):
        assert authentication_client.logout("invalid") is False