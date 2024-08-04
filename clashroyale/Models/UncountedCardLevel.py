from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(kw_only=True)
class UncountedCardLevel(Object):
    level: int
    star_level: int | None = None
    evolution_level: int | None = None
