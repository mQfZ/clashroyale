from datetime import datetime as BaseDatetime
from typing import Annotated, Any

from pydantic import ValidatorFunctionWrapHandler, WrapValidator


def validate_datetime(value: Any, _: ValidatorFunctionWrapHandler):
    return BaseDatetime.strptime(value, "%Y%m%dT%H%M%S.%fZ")


DateTime = Annotated[BaseDatetime, WrapValidator(validate_datetime)]
