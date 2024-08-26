from pydantic.dataclasses import dataclass

from .Challenge import Challenge
from .DateTime import DateTime
from .Object import Object


@dataclass(frozen=True, kw_only=True)
class ChallengeChain(Object):
    type: str
    start_time: DateTime
    end_time: DateTime
    challenges: list[Challenge]
