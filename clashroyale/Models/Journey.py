from pydantic.dataclasses import dataclass

from .Arena import Arena
from .Object import Object


@dataclass(frozen=True, kw_only=True)
class Journey(Object):
    arena: Arena
    trophies: int
    best_trophies: int
