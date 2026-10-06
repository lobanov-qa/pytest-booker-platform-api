from collections.abc import Callable, Mapping
from typing import Any, TypeVar

from httpx import URL, Client, Response
from httpx._types import QueryParamTypes, RequestData, RequestFiles
from pydantic import BaseModel

import allure


T = TypeVar("T", bound=BaseModel)


class APIClient:
    """Thin httpx.Client wrapper adding base URL, timeout and event hooks."""

    def __init__(
        self,
        base_url: str,
        timeout: float,
        event_hooks: Mapping[str, list[Callable[..., None]]] | None = None,
        **kwargs: Any,
    ) -> None:
        self.client = Client(
            base_url=base_url, timeout=timeout, event_hooks=event_hooks, **kwargs
        )

    @allure.step("Make GET request to {url}")
    def get(
        self,
        url: URL | str,
        params: QueryParamTypes | None = None,
    ) -> Response:
        """
        Performs a GET request.

        :param url: Endpoint URL.
        :param params: Query parameters (e.g. ?key=value).
        :return: Response object with response data.
        """
        return self.client.get(url, params=params)

    @allure.step("Make POST request to {url}")
    def post(
        self,
        url: URL | str,
        json: Any | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
    ) -> Response:
        """
        Performs a POST request.

        :param url: Endpoint URL.
        :param json: JSON data to send.
        :param data: Form data (e.g. application/x-www-form-urlencoded).
        :param files: Files to upload.
        :return: Response object with response data.
        """
        return self.client.post(url, json=json, data=data, files=files)

    @allure.step("Make PUT request to {url}")
    def put(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Performs a PUT request (full update).

        :param url: Endpoint URL.
        :param json: JSON data to update.
        :return: Response object with response data.
        """
        return self.client.put(url, json=json)

    @allure.step("Make PATCH request to {url}")
    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Performs a PATCH request (partial update).

        :param url: Endpoint URL.
        :param json: JSON data to patch.
        :return: Response object with response data.
        """
        return self.client.patch(url, json=json)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: URL | str) -> Response:
        """
        Performs a DELETE request (deletes data).

        :param url: Endpoint URL.
        :return: Response object with response data.
        """
        return self.client.delete(url)

    @staticmethod
    def parse_response(response: Response, model: type[T]) -> T:
        """
        Parse JSON response and validate against Pydantic model.

        Raises HTTPStatusError if status is not 2xx.

        :param response: HTTP response from httpx.
        :param model: Target Pydantic model (e.g. CreateBookingResponseSchema).
        :return: Parsed and validated model instance of the correct type.
        """
        response.raise_for_status()
        return model.model_validate(response.json())

    def close(self) -> None:
        """Closes the underlying HTTP client."""
        self.client.close()
