from pydantic.dataclasses import dataclass

from .Arena import Arena
from .NamedPlayer import NamedPlayer


@dataclass(kw_only=True)
class OutlinedPlayer(NamedPlayer):
    exp_level: int
    trophies: int
    arena: Arena

    role: str
    donations: int
    donations_received: int
