from enum import StrEnum


class MessageRoutes(StrEnum):
    ROOT = "/"
    MESSAGE_ID = "/{id}"
    MESSAGE_READ = "/{id}/read"
    COUNT = "/count"

    def __str__(self):
        return self.value