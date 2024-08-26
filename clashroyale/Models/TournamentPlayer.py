from pydantic.dataclasses import dataclass

from .BadgedClanPlayer import BadgedClanPlayer


@dataclass(frozen=True, kw_only=True)
class TournamentPlayer(BadgedClanPlayer):
    score: int
    rank: int
