from pydantic.dataclasses import dataclass

from .BattleTeamRoundSummary import BattleTeamRoundSummary


@dataclass(kw_only=True)
class BattleRound(BattleTeamRoundSummary):
    pass
