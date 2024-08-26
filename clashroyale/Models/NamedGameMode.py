from pydantic.dataclasses import dataclass

from .IDedGameMode import IDedGameMode


@dataclass(frozen=True, kw_only=True)
class NamedGameMode(IDedGameMode):
    name: str
