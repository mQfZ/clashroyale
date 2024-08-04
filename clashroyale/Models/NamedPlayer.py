from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(kw_only=True)
class NamedPlayer(Object):
    tag: str
    name: str
