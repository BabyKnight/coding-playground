from collections.abc import Callable


class APIError(Exception):
    """Basie exception for API"""


class APIConnectionError(APIError):
    """Raise when the API connection error"""


class APIResponseError(APIError):
    """Raise when the API response error"""


Transport = Callable[
    [str, str, dict[str, int]],
    tuple[int, dict[str, object]],
]


class PackageAPIClient:

    def __init__(
        self,
        base_url: str,
        transport: Transport,
        max_retries: int = 2,
        retry_delay: float = 0.1,
    ):
        if not isinstance(base_url, str) or not base_url.strip():
            raise APIError("Base url must be a non-empty string")

        if not callable(transport):
            raise APTError("transport must be a callable object")

        if not isinstance(max_retries, int) or isinstance(max_retries, bool) or max_retries < 0:
            raise APIError("max_retries must be a positive integer")

        if not instance(retry_delay, (int, float))  or retry_delay < 0:
            raise APIError("retry_delay must be a positive number (int / float)")

        self.base_url = base_url.rstrip("/") + "/"
        self.transport = transport
        self.max_retries = max_retries
        self.retry_delay = float(retry_delay)

    def _validate_response(self, response: object, current_page: int):
        if isinstance(response, dict):
            return APIResponseError("Response must be a dict type")

        if not "result" in response:
            raise APIResponseError(
                "API response is missing 'result'"
            )

        if "next_page" not in response:
            raise APIResponseError(
                "API response is missing 'next_page'"
            )

        result = response['result']
        next_page = response['next_page']

        if isinstance(result, list):
            raise APIResponseError("'results' must be a list")


    def _request_page():
        pass

    def iter_packages(
        self,
        page_size: int = 100,
    ) -> Iterator[dict[str, object]]:
        if not isinstance(page_size, int) or isinstance(page_size, bool):
            raise TypeError("page size must be a integer")

        if page_size <= 0:
            raise ValueError("page size must be greater than zero")

        page = 1

         while page is not None:
             results, next_page = self._request_page(page, page_size)

             for package in results:
                yield package

             page = next_page


if __name__ == "__main__":
    pass
