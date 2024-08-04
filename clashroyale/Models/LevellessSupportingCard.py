from pydantic.dataclasses import dataclass

from .OutlinedCard import OutlinedCard


@dataclass(kw_only=True)
class LevellessSupportingCard(OutlinedCard):
    pass
