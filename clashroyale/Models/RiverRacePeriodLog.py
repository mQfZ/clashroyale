from pydantic.dataclasses import dataclass

from .ItemedList import ItemedList
from .RiverRacePeriodLogEntry import RiverRacePeriodLogEntry


@dataclass(frozen=True, kw_only=True)
class RiverRacePeriodLog(ItemedList[RiverRacePeriodLogEntry]):
    period_index: int
