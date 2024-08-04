from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(kw_only=True)
class SeasonlessPlayerLeagueResult(Object):
    rank: int | None = None
    trophies: int
    best_trophies: int | None = None
