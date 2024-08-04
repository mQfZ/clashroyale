from pydantic.dataclasses import dataclass

from .LevellessSupportingCard import LevellessSupportingCard
from .UncountedCardLevel import UncountedCardLevel


@dataclass(kw_only=True)
class UncountedLeveledSupportingCard(UncountedCardLevel, LevellessSupportingCard):
    pass
