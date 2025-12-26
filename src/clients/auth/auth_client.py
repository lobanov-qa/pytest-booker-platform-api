from httpx import Response, HTTPStatusError

from clients.api_client import APIClient

from clients.auth.auth_schema import LoginRequestSchema, ValidateRequestSchema, LogoutRequestSchema
from clients.auth.routes import AuthRoutes


class AuthClient(APIClient):
    """
    HTTP client for interacting with the authentication service.

    Provides methods for performing authentication operations,
    Based on the base APIClient client.
    """
    def __init__(self, base_url: str, timeout: float):
        super().__init__(base_url=base_url, timeout=timeout)
        self.token = None


    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Performs an HTTP request to authenticate the user.

        :param request: LoginRequestSchema object containing
                        username and password.
        :return: A response object from the server containing the status, headers, and body.
        """
        return self.post(AuthRoutes.LOGIN, json=request.model_dump())



    def login(self, request: LoginRequestSchema) -> str:
        """
        Authenticates the user and retrieves the session token from the cookie.
        :param request: LoginRequestSchema object with credentials.
        :return: String value of the session token.
        :raises Exception: If the response status is not 200 or the token is not found.
        """
        response = self.login_api(request)
        response.raise_for_status()
        cookies = response.cookies
        token = cookies.get("token")
        if not token:
            raise Exception("Token not found in response cookies")
        self.token = token
        return token

    def validate_api(self, request: ValidateRequestSchema) -> Response:
        """
        Sends a token validation request to the server.
        :param request: ValidateRequestSchema object containing the token.
        :return: Raw response from the server.
        """
        return self.post(AuthRoutes.VALIDATE, json=request.model_dump())

    def is_token_valid(self, token: str) -> bool:
        """
        Validates a token and returns True if validation was successful (200 OK).
        :param token: Token string to validate.
        :return: True if token is valid, False otherwise.
        """
        if not token:
            return False
        request = ValidateRequestSchema(token=token)
        try:
            response = self.validate_api(request)
            return response.status_code == 200
        except HTTPStatusError:
            return False
    def logout_api(self, request: LogoutRequestSchema) -> Response:
        """
        Sends a token logout request to the server.
        :param request: LogoutRequestSchema object containing the token.
        :return: Raw response from the server.
        """
        return self.post(AuthRoutes.LOGOUT, json=request.model_dump())

    def logout(self, token: str) -> bool:
        """
        Logs out the user by sending a logout request to the server.

        :param token: Token string to be used for logout.
        :return: True if logout was successful (200 OK), False otherwise.
        """
        if not token:
            return False
        request = LogoutRequestSchema(token=token)
        try:
            response = self.logout_api(request)
            return response.status_code == 200
        except HTTPStatusError:
            return False