from pydantic import BaseModel, Field

from config import settings


class LoginRequestSchema(BaseModel):
    """
    Schema for authentication request (POST /auth/login).
    """
    username: str = Field(default=settings.test_user.login)
    password: str = Field(default=settings.test_user.password)


class ValidateRequestSchema(BaseModel):
    """
    Schema for token validation request (POST /auth/validate).
    """
    token: str = Field(...)


class LogoutRequestSchema(BaseModel):
    """
    Schema for logout request (POST /auth/logout).
    """
    token: str = Field(...)