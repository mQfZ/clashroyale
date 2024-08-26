from pydantic import Field
from pydantic.dataclasses import dataclass

from .BadgedClanPlayer import BadgedClanPlayer
from .BattleRound import BattleRound
from .UncountedLeveledPlayingCard import UncountedLeveledPlayingCard
from .UncountedLeveledSupportingCard import UncountedLeveledSupportingCard


@dataclass(frozen=True, kw_only=True)
class BattlePlayer(BadgedClanPlayer):
    starting_trophies: int | None = None
    trophy_change: int | None = None
    global_rank: int | None

    playing_cards: list[UncountedLeveledPlayingCard] = Field(alias="cards")
    supporting_cards: list[UncountedLeveledSupportingCard] = Field(default_factory=list, alias="supportCards")

    crowns: int
    king_tower_hit_points: int
    princess_towers_hit_points: list[int] | None
    elixir_leaked: float

    rounds: list[BattleRound] | None = None
