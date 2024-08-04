from pydantic.dataclasses import dataclass

from .BadgedClanPlayer import BadgedClanPlayer


@dataclass(kw_only=True)
class RankedJourneyLeaderboardPlayer(BadgedClanPlayer):
    rank: int
    score: int
