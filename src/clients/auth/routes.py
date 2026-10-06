from enum import StrEnum


class AuthRoutes(StrEnum):
    """Endpoints of the auth-service."""

    LOGIN = "/login"
    VALIDATE = "/validate"
    LOGOUT = "/logout"

    def __str__(self):
        return self.value
