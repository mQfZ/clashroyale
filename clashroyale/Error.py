from pydantic import ValidationError as PydanticValidationError


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


class ValidationError(ClashRoyaleError):
    def __init__(self, path: str, validation_error: PydanticValidationError) -> None:
        self.path = path
        self.validation_error = validation_error

        text = f"{self.path}\n{self.validation_error}"
        super().__init__(text)
