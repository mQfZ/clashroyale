from pydantic import Field
from pydantic.dataclasses import dataclass

from .UncountedLeveledPlayingCard import UncountedLeveledPlayingCard
from .UncountedLeveledSupportingCard import UncountedLeveledSupportingCard


@dataclass(kw_only=True)
class BattleTeamRoundSummary:
    playing_cards: list[UncountedLeveledPlayingCard] = Field(alias="cards")
    supporting_cards: list[UncountedLeveledSupportingCard] | None = Field(alias="supportCards")

    crowns: int
    king_tower_hit_points: int
    princess_towers_hit_points: list[int] | None
    elixir_leaked: float
