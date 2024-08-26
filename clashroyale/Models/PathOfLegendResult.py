from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(frozen=True, kw_only=True)
class PathOfLegendResult(Object):
    league_number: int
    trophies: int
    rank: int | None
