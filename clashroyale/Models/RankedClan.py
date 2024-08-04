from pydantic.dataclasses import dataclass

from .BadgedClan import BadgedClan
from .Location import Location


@dataclass(kw_only=True)
class RankedClan(BadgedClan):
    rank: int
    previous_rank: int
    location: Location
    clan_score: int
    members: int
