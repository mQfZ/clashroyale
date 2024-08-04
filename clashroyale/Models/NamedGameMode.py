from pydantic.dataclasses import dataclass

from .IDedGameMode import IDedGameMode


@dataclass(kw_only=True)
class NamedGameMode(IDedGameMode):
    name: str
