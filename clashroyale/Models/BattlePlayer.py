from pydantic.dataclasses import dataclass

from .BadgedClanPlayer import BadgedClanPlayer
from .BattleRound import BattleRound
from .BattleTeamRoundSummary import BattleTeamRoundSummary


@dataclass(kw_only=True)
class BattlePlayer(BadgedClanPlayer, BattleTeamRoundSummary):
    starting_trophies: int | None = None
    trophy_change: int | None = None
    global_rank: int | None

    rounds: list[BattleRound] | None = None
