class CustomConnector():
    def __init__(self):
        pass

    def raise_error(self, config: dict, params: dict):
        return {"hello": "error"}

    def do_something(self, config: dict, params: dict):
        return {"hello": "world"}