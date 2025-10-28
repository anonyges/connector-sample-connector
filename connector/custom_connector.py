import requests
from typing import Literal, Optional, Union


class CustomConnector:
    def __init__(self, url: str, api_key: str, verify_ssl: bool):
        self.url: str = url
        self.api_key: str = api_key
        self.verify_ssl: bool = verify_ssl
        self._check_url(url)

    def _check_url(self, url: str):
        if not (url.startswith("https://") or url.startswith("http://")):
            raise Exception("config url must start with 'https://' or 'http://'")

        if url.endswith("/"):
            raise Exception("config url must not end with '/'")

    def _check_api_endpoint(self, api_endpoint: str):
        if not api_endpoint.startswith("/"):
            raise Exception("param api_endpoint must startswith '/'")

    def _delete_none_dict(self, _d: Union[dict, list, None]) -> Union[dict, list, None]:
        if _d == None:
            return None
        elif isinstance(_d, list):
            return _d
        return {k: v for k, v in _d.items() if v is not None}

    def _check_health(self):
        return self.health_check()

    def generic_api_call(
        self,
        method: Literal["GET", "PUT", "POST", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE"],
        api_endpoint: str,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        json_data: Optional[dict] = None,
    ) -> dict:
        self._check_api_endpoint(api_endpoint)
        url = self.url + "/vm" + api_endpoint

        headers = headers if headers else {}
        headers["X-Api-Key"] = self.api_key
        headers["content-type"] = "application/json"

        params_new = self._delete_none_dict(params)
        json_data_new = self._delete_none_dict(json_data)

        resp = requests.request(method, url, headers=headers, params=params_new, json=json_data_new, verify=self.verify_ssl)
        return resp.json()

    def health_check(self) -> dict:
        endpoint = f"/admin/health"
        return self.generic_api_call("GET", endpoint)

    def do_something(self, params: dict) -> dict:
        return {"hello": "world"}

    def raise_error(self, params: dict) -> dict:
        return {"hello": "error"}
