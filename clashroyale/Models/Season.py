from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(kw_only=True)
class Season(Object):
    id: str
