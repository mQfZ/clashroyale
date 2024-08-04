from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(kw_only=True)
class Error(Object):
    reason: str
    message: str | None = None
