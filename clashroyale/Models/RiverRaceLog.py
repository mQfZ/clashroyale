from pydantic.dataclasses import dataclass

from .DateTime import DateTime
from .Object import Object
from .RiverRaceStanding import RiverRaceStanding


@dataclass(kw_only=True)
class RiverRaceLog(Object):
    season_id: int
    section_index: int
    created_date: DateTime

    standings: list[RiverRaceStanding]
