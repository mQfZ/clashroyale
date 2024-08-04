from pydantic.dataclasses import dataclass

from .OutlinedCard import OutlinedCard


@dataclass(kw_only=True)
class LevellessPlayingCard(OutlinedCard):
    elixir_cost: int | None = None
