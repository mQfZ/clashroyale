from pydantic import Field
from pydantic.dataclasses import dataclass

from .Object import Object
from .UncountedLeveledPlayingCard import UncountedLeveledPlayingCard
from .UncountedLeveledSupportingCard import UncountedLeveledSupportingCard


@dataclass(kw_only=True)
class BattleRound(Object):
    playing_cards: list[UncountedLeveledPlayingCard] = Field(alias="cards")
    supporting_cards: list[UncountedLeveledSupportingCard] = Field(default_factory=list, alias="supportCards")

    crowns: int
    king_tower_hit_points: int | None = None
    princess_towers_hit_points: list[int] | None
    elixir_leaked: float
