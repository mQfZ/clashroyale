from pydantic.dataclasses import dataclass

from .OutlinedCard import OutlinedCard


@dataclass(frozen=True, kw_only=True)
class LevellessSupportingCard(OutlinedCard):
    pass
