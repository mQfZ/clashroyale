class ClashRoyaleError(Exception):
    pass


class APIError(ClashRoyaleError):
    def __init__(self, path: str, reason: str, message: str | None):
        self.path = path
        self.reason = reason
        self.message = message

        text = f"{self.path}: {self.reason}"
        if self.message is not None:
            text += f": {self.message}"
        super().__init__(text)
