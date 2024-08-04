from pydantic.dataclasses import dataclass

from .Object import Object
from .RiverRaceClan import RiverRaceClan


@dataclass(kw_only=True)
class RiverRaceStanding(Object):
    rank: int
    trophy_change: int
    clan: RiverRaceClan
