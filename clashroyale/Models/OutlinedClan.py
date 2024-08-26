from pydantic.dataclasses import dataclass

from .BadgedClan import BadgedClan
from .Location import Location


@dataclass(frozen=True, kw_only=True)
class OutlinedClan(BadgedClan):
    type: str
    location: Location
    required_trophies: int
    members: int

    donations_per_week: int
    clan_score: int
    clan_war_trophies: int
    clan_chest_level: int
    clan_chest_max_level: int
