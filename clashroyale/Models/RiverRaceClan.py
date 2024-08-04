from pydantic.dataclasses import dataclass

from .BadgedClan import BadgedClan
from .DateTime import DateTime
from .RiverRacePlayer import RiverRacePlayer


@dataclass(kw_only=True)
class RiverRaceClan(BadgedClan):
    finish_time: DateTime | None = None
    clan_score: int
    fame: int
    repair_points: int
    period_points: int

    participants: list[RiverRacePlayer]
