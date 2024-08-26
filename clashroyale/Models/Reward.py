from pydantic.dataclasses import dataclass

from .OutlinedCard import OutlinedCard


@dataclass(frozen=True, kw_only=True)
class Reward:
    type: str | None
    wins: int | None = None
    amount: int | None = None
    card: OutlinedCard | None = None
    resource: str | None = None
    consumable_name: str | None = None
    rarity: str | None = None
