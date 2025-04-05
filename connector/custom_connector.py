import requests

class CustomConnector():
    def __init__(self):
        pass

    def check_health(self, config: dict, params: dict=None) -> dict:
        pass

    def generic_api_call(self, config: dict, params: dict) -> dict:
        c_url = config.get("url")
        c_api_key = config.get("api_key")
        c_verify_ssl = config.get("verify_ssl")
        
        p_api_endpoint = params.get("api_endpoint")
        p_method = params.get("method")
        p_headers = params.get("headers") # dict or None
        p_params = params.get("params") # dict or None
        p_data = params.get("data") # dict or None

        c_url = c_url + p_api_endpoint

        resp = requests.request(p_method, c_url, headers=p_headers, params=p_params, data=p_data, verify=c_verify_ssl)
        return resp.json()

    def raise_error(self, config: dict, params: dict) -> dict:
        return {"hello": "error"}

    def do_something(self, config: dict, params: dict) -> dict:
        return {"hello": "world"}