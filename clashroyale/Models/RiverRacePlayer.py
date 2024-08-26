from pydantic.dataclasses import dataclass

from .NamedPlayer import NamedPlayer


@dataclass(frozen=True, kw_only=True)
class RiverRacePlayer(NamedPlayer):
    fame: int
    repair_points: int
    boat_attacks: int
    decks_used: int
    decks_used_today: int
