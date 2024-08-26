from pydantic import Field, HttpUrl
from pydantic.dataclasses import dataclass

from .IDedCard import IDedCard


@dataclass(frozen=True, kw_only=True)
class OutlinedCard(IDedCard):
    id: int
    name: str | None = None
    rarity: str | None = None

    max_level: int
    max_evolution_level: int | None = None

    icon_urls: dict[str, HttpUrl] = Field(default_factory=dict)
