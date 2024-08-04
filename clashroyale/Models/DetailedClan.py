from pydantic.dataclasses import dataclass

from .ClanPlayer import ClanPlayer
from .OutlinedClan import OutlinedClan


@dataclass(kw_only=True)
class DetailedClan(OutlinedClan):
    description: str
    clan_chest_status: str | None = None
    member_list: list[ClanPlayer]
