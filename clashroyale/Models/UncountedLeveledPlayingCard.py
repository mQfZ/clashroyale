from pydantic.dataclasses import dataclass

from .LevellessPlayingCard import LevellessPlayingCard
from .UncountedCardLevel import UncountedCardLevel


@dataclass(frozen=True, kw_only=True)
class UncountedLeveledPlayingCard(UncountedCardLevel, LevellessPlayingCard):
    pass
