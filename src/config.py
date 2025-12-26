from pathlib import Path
from typing import  Optional
from pydantic import BaseModel, AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Укажите путь к .env явно
BASE_DIR = Path(__file__).parent.parent  # → /src → / (корень)
ENV_FILE = BASE_DIR / ".env"

print(f"Загружаю .env из: {ENV_FILE}")  # ← Отладка: увидите путь
if not ENV_FILE.exists():
    raise RuntimeError(f"Файл .env не найден по пути: {ENV_FILE}")

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

    test_user: TestDataConfig = TestDataConfig()

settings = Settings()



