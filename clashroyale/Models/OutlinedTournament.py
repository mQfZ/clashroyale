from pydantic.dataclasses import dataclass

from .DateTime import DateTime
from .IDedGameMode import IDedGameMode
from .Object import Object


@dataclass(kw_only=True)
class OutlinedTournament(Object):
    tag: str
    name: str
    description: str

    type: str
    status: str
    created_time: DateTime
    creator_tag: str

    level_cap: int
    game_mode: IDedGameMode
    capacity: int
    max_capacity: int
    preparation_duration: int
    duration: int

    first_place_card_prize: int
