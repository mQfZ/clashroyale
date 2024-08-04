from pydantic.dataclasses import dataclass

from .Object import Object
from .SeasonlessPlayerLeagueResult import SeasonlessPlayerLeagueResult
from .SeasonedPlayerLeagueResult import SeasonedPlayerLeagueResult


@dataclass(kw_only=True)
class PlayerLeagueStatistics(Object):
    current_season: SeasonlessPlayerLeagueResult
    previous_season: SeasonedPlayerLeagueResult
    best_season: SeasonedPlayerLeagueResult
