from enum import StrEnum



class AuthRoutes(StrEnum):
    LOGIN = "/login"
    VALIDATE = "/validate"
    LOGOUT = "/logout"

    def __str__(self):
        return self.value