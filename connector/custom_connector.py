import requests

class CustomConnector():
    def __init__(self):
        pass

    def health_check(self, config: dict, params: dict=None) -> dict:
        pass

    def generic_api_call(self, config: dict, params: dict) -> dict:
        url = config.get("url")
        api_key = config.get("api_key")
        verify_ssl = config.get("verify_ssl")
        
        r_api_endpoint = params.get("api_endpoint")
        r_method = params.get("method")
        r_headers = params.get("headers") # dict or None
        r_params = params.get("params") # dict or None
        r_data = params.get("data") # dict or None

        r_url = url + r_api_endpoint

        resp = requests.request(r_method, r_url, headers=r_headers, params=r_params, data=r_data, verify=verify_ssl)
        return resp.json()

    def raise_error(self, config: dict, params: dict) -> dict:
        return {"hello": "error"}

    def do_something(self, config: dict, params: dict) -> dict:
        return {"hello": "world"}