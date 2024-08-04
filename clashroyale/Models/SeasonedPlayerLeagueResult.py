from pydantic.dataclasses import dataclass

from .Season import Season
from .SeasonlessPlayerLeagueResult import SeasonlessPlayerLeagueResult


@dataclass(kw_only=True)
class SeasonedPlayerLeagueResult(Season, SeasonlessPlayerLeagueResult):
    pass
