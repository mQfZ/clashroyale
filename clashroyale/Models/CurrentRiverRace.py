from pydantic.dataclasses import dataclass

from .Object import Object
from .RiverRaceClan import RiverRaceClan
from .RiverRacePeriodLog import RiverRacePeriodLog


@dataclass(frozen=True, kw_only=True)
class CurrentRiverRace(Object):
    state: str

    clan: RiverRaceClan
    clans: list[RiverRaceClan]

    section_index: int
    period_index: int
    period_type: str
    period_logs: list[RiverRacePeriodLog]
