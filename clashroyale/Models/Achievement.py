from pydantic import Field
from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(frozen=True, kw_only=True)
class Achievement(Object):
    name: str
    description: str = Field(alias="info")

    stars: int
    value: int
    target: int
