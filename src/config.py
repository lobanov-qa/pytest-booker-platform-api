from typing import Self

from pathlib import Path
from typing import  Optional
from pydantic import BaseModel, AnyHttpUrl, Field, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent
ENV_FILE = BASE_DIR / ".env"



class HTTPClientConfig(BaseModel):
    timeout: float = Field(30.0, description="Default timeout for all requests")
    retries: int = Field(3, description="Default retry count")

    

class ServiceSettings(BaseModel):
    url: AnyHttpUrl
    timeout: Optional[float] = None  

    def get_timeout(self, default_timeout: float) -> float:
        return self.timeout if self.timeout is not None else default_timeout

    @property
    def client_url(self) -> str:
        return str(self.url)
    

class TestDataConfig(BaseModel):
    login: str = Field(default="admin")
    password: str = Field(default="password")

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='allow',
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        env_nested_delimiter="."
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
    def initialize(cls) -> Self:
        allure_results_dir = DirectoryPath("./allure-results")
        allure_results_dir.mkdir(exist_ok=True)

        # Передаем allure_results_dir в инициализацию настроек
        return Settings(allure_results_dir=allure_results_dir)


settings = Settings.initialize()




