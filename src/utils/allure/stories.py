from enum import StrEnum


class AllureStory(StrEnum):
    # Authentication Stories
    LOGIN_WITH_VALID_CREDENTIALS = "User login to the system"
    USER_LOGOUT = "User logout from the system"
    TOKEN_VALIDATION = "Token validation process"