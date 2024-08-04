from pydantic.dataclasses import dataclass

from .DateTime import DateTime
from .OutlinedPlayer import OutlinedPlayer


@dataclass(kw_only=True)
class ClanPlayer(OutlinedPlayer):
    last_seen: DateTime | None = None
    clan_rank: int
    previous_clan_rank: int
    clan_chest_points: int
