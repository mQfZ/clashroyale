from pydantic.dataclasses import dataclass

from .Arena import Arena
from .Object import Object


@dataclass(kw_only=True)
class Journey(Object):
    arena: Arena
    trophies: int
    best_trophies: int
