from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(kw_only=True)
class IDedCard(Object):
    id: int
