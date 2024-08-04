from pydantic.dataclasses import dataclass

from .LevellessPlayingCard import LevellessPlayingCard
from .UncountedCardLevel import UncountedCardLevel


@dataclass(kw_only=True)
class UncountedLeveledPlayingCard(UncountedCardLevel, LevellessPlayingCard):
    pass
