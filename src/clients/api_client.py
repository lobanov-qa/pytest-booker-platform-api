from typing import Any, Mapping, Type, TypeVar
from pydantic import BaseModel
import allure

from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles

T = TypeVar("T", bound=BaseModel)

class APIClient:
    def __init__(
            self,
            base_url: str,
            timeout: float,
            event_hooks: Mapping[str, list] | None = None,
            **kwargs: Any
    ):
        self.client = Client(
            base_url=base_url,
            timeout=timeout,
            event_hooks=event_hooks,
            **kwargs
        )

    @allure.step("Make GET request to {url}")
    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
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
            files: RequestFiles | None = None
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
    def parse_response(response: Response, model: Type[T]) -> T:
        """
        Parse JSON response and validate against Pydantic model.
        Raises HTTPStatusError if status is not 2xx.

        :param response: HTTP response from httpx.
        :param model: Target Pydantic model (e.g. CreateBookingResponseSchema).
        :return: Parsed and validated model instance of the correct type.
        """
        response.raise_for_status()
        return model.model_validate(response.json())

    def close(self):
        self.client.close()