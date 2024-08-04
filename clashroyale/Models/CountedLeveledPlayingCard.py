from pydantic.dataclasses import dataclass

from .CountedCardLevel import CountedCardLevel
from .LevellessPlayingCard import LevellessPlayingCard


@dataclass(kw_only=True)
class CountedLeveledPlayingCard(CountedCardLevel, LevellessPlayingCard):
    pass
