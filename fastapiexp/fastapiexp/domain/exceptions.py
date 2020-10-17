class BaseError(Exception):

    code: str = ""

    def __init__(self, description: str):
        self.description = description


class StoreError(BaseError):

    code: str = "STORE_ERROR"
