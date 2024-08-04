from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(kw_only=True)
class JourneyLeaderboard(Object):
    id: int
    name: str
