from pydantic.dataclasses import dataclass

from .BadgedClanPlayer import BadgedClanPlayer


@dataclass(kw_only=True)
class RankedPlayer(BadgedClanPlayer):
    exp_level: int
    elo_rating: int
    rank: int
