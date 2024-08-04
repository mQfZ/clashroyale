from pydantic.dataclasses import dataclass

from .DateTime import DateTime
from .OutlinedTournament import OutlinedTournament
from .TournamentPlayer import TournamentPlayer


@dataclass(kw_only=True)
class DetailedTournament(OutlinedTournament):
    started_time: DateTime
    members_list: list[TournamentPlayer]
