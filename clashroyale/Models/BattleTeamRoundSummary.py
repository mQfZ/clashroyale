from pydantic import Field
from pydantic.dataclasses import dataclass

from .Object import Object
from .UncountedLeveledPlayingCard import UncountedLeveledPlayingCard
from .UncountedLeveledSupportingCard import UncountedLeveledSupportingCard


@dataclass(kw_only=True)
class BattleTeamRoundSummary(Object):
    playing_cards: list[UncountedLeveledPlayingCard] = Field(alias="cards")
    supporting_cards: list[UncountedLeveledSupportingCard] | None = Field(None, alias="supportCards")

    crowns: int
    king_tower_hit_points: int
    princess_towers_hit_points: list[int] | None
    elixir_leaked: float
