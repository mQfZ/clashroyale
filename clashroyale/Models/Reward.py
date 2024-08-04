from pydantic.dataclasses import dataclass

from .IDedCard import IDedCard


@dataclass(kw_only=True)
class Reward:
    type: str | None
    wins: int | None = None
    amount: int | None = None
    card: IDedCard | None = None
    resource: str | None = None
    consumable_name: str | None = None
    rarity: str | None = None
