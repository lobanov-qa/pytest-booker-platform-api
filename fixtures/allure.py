from collections.abc import Generator
from typing import Any

import pytest

from utils.allure.environment import create_allure_environment_file


@pytest.fixture(scope="session", autouse=True)
def save_allure_environment_file() -> Generator[Any, None, None]:
    yield
    create_allure_environment_file()
