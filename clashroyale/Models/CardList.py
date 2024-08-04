from pydantic import Field
from pydantic.dataclasses import dataclass

from .LevellessPlayingCard import LevellessPlayingCard
from .LevellessSupportingCard import LevellessSupportingCard
from .Object import Object


@dataclass(kw_only=True)
class CardList(Object):
    playing_cards: list[LevellessPlayingCard] = Field(alias="items")
    supporting_cards: list[LevellessSupportingCard] = Field(alias="supportItems")
