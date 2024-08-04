from pydantic.dataclasses import dataclass

from .CountedCardLevel import CountedCardLevel
from .LevellessSupportingCard import LevellessSupportingCard


@dataclass(kw_only=True)
class CountedLeveledSupportingCard(CountedCardLevel, LevellessSupportingCard):
    pass
