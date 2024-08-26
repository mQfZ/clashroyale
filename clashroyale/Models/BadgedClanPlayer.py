from pydantic.dataclasses import dataclass

from .BadgedClan import BadgedClan
from .NamedPlayer import NamedPlayer


@dataclass(frozen=True, kw_only=True)
class BadgedClanPlayer(NamedPlayer):
    clan: BadgedClan | None = None
