from pydantic import HttpUrl
from pydantic.dataclasses import dataclass

from .NamedGameMode import NamedGameMode
from .Object import Object
from .Reward import Reward


@dataclass(frozen=True, kw_only=True)
class Challenge(Object):
    id: int
    name: str
    description: str

    game_mode: NamedGameMode
    win_mode: str
    casual: bool
    max_losses: int
    max_wins: int

    prizes: list[Reward]

    icon_url: HttpUrl
