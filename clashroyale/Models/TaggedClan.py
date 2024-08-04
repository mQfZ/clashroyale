from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(kw_only=True)
class TaggedClan(Object):
    tag: str
