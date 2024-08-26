from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(frozen=True, kw_only=True)
class Arena(Object):
    id: int
    name: str
