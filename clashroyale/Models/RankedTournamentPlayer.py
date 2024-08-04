from pydantic.dataclasses import dataclass

from .BadgedClanPlayer import BadgedClanPlayer


@dataclass(kw_only=True)
class RankedTournamentPlayer(BadgedClanPlayer):
    wins: int
    losses: int
    rank: int
    previous_rank: int
