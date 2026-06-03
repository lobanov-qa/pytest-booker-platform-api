from enum import StrEnum


class BrandingRoutes(StrEnum):
    """Branding API routes."""
    ROOT = "/"

    def __str__(self):
        return self.value