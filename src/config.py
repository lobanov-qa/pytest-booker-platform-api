from pathlib import Path

from pydantic import AnyHttpUrl, BaseModel, DirectoryPath, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent
ENV_FILE = BASE_DIR / ".env"


class HTTPClientConfig(BaseModel):
    """Default HTTP client behavior: timeout and retry count."""

    timeout: float = Field(30.0, description="Default timeout for all requests")
    retries: int = Field(3, description="Default retry count")


class ServiceSettings(BaseModel):
    """Base URL and optional per-service timeout override."""

    url: AnyHttpUrl
    timeout: float | None = None

    def get_timeout(self, default_timeout: float) -> float:
        """Returns the service timeout or the default when unset."""
        return self.timeout if self.timeout is not None else default_timeout

    @property
    def client_url(self) -> str:
        """Returns the service URL as a plain string."""
        return str(self.url)


class TestDataConfig(BaseModel):
    """Credentials of the seeded test user."""

    login: str = Field(default="admin")
    password: str = Field(default="password")


class Settings(BaseSettings):
    """Root settings loaded from environment variables and .env file."""

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    http_client: HTTPClientConfig = HTTPClientConfig()

    booking: ServiceSettings
    auth: ServiceSettings
    room: ServiceSettings
    report: ServiceSettings
    branding: ServiceSettings
    message: ServiceSettings

    allure_results_dir: DirectoryPath

    test_user: TestDataConfig = TestDataConfig()

    @classmethod
    def initialize(cls) -> "Settings":
        """Creates the Allure results directory and loads settings."""
        allure_results_dir = DirectoryPath("./allure-results")
        allure_results_dir.mkdir(exist_ok=True)

        # Pass the results dir explicitly so the model validates it
        return Settings(allure_results_dir=allure_results_dir)


settings = Settings.initialize()
