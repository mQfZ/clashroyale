from pydantic.dataclasses import dataclass

from .Object import Object
from .TaggedClan import TaggedClan


@dataclass(frozen=True, kw_only=True)
class RiverRacePeriodLogEntry(Object):
    clan: TaggedClan

    points_earned: int
    progress_start_of_day: int
    progress_end_of_day: int
    end_of_day_rank: int
    progress_earned: int
    num_of_defenses_remaining: int
    progress_earned_from_defenses: int
