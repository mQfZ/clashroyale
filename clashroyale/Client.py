from typing import Literal
from urllib.parse import quote

from pydantic import TypeAdapter
from requests import Session

from .Error import APIError
from .Models import (
    Battle,
    CardList,
    ChallengeChain,
    ClanPlayer,
    CurrentRiverRace,
    DetailedClan,
    DetailedPlayer,
    DetailedTournament,
    GlobalTournament,
    Error,
    IndexedChest,
    ItemedList,
    JourneyLeaderboard,
    Location,
    OutlinedClan,
    OutlinedTournament,
    PaginatedList,
    RankedClan,
    RankedJourneyLeaderboardPlayer,
    RankedPlayer,
    RankedTournamentPlayer,
    RiverRaceLog,
    Season,
)


class ClashRoyale:
    BASE_URL = "https://api.clashroyale.com/v1"

    def __init__(self, api_key: str):
        self._session = Session()
        self._session.headers["Authorization"] = "Bearer " + api_key

    def _get[T](self, model: type[T], path: str, params: dict | None = None) -> T:
        response = self._session.get(self.BASE_URL + quote(path), params=params)
        if response.status_code == 200:
            return TypeAdapter(model).validate_json(response.content)
        else:
            error = TypeAdapter(Error).validate_json(response.content)
            raise APIError(path, error.reason, error.message)

    def get_clans(
        self,
        *,
        name: str | None = None,
        location_id: int | None = None,
        min_members: int | None = None,
        max_members: int | None = None,
        min_score: int | None = None,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[OutlinedClan]:
        return self._get(
            PaginatedList[OutlinedClan],
            "/clans",
            {
                "name": name,
                "locationId": location_id,
                "minMembers": min_members,
                "maxMembers": max_members,
                "minScore": min_score,
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_river_race_log(
        self,
        clan_tag: str,
        *,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[RiverRaceLog]:
        return self._get(
            PaginatedList[RiverRaceLog],
            f"/clans/{quote(clan_tag, safe='#')}/riverracelog",
            {
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_clan(
        self,
        clan_tag: str,
    ) -> DetailedClan:
        return self._get(
            DetailedClan,
            f"/clans/{quote(clan_tag, safe='#')}",
        )

    def get_clan_members(
        self,
        clan_tag: str,
        *,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[ClanPlayer]:
        return self._get(
            PaginatedList[ClanPlayer],
            f"/clans/{quote(clan_tag, safe='#')}/members",
            {
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_current_river_race(
        self,
        clan_tag: str,
    ) -> CurrentRiverRace:
        return self._get(
            CurrentRiverRace,
            f"/clans/{quote(clan_tag, safe='#')}/currentriverrace",
        )

    def get_player(
        self,
        player_tag: str,
    ) -> DetailedPlayer:
        return self._get(
            DetailedPlayer,
            f"/players/{quote(player_tag, safe='#')}",
        )

    def get_upcoming_chests(
        self,
        player_tag: str,
    ) -> ItemedList[IndexedChest]:
        return self._get(
            ItemedList[IndexedChest],
            f"/players/{quote(player_tag, safe='#')}/upcomingchests",
        )

    def get_battle_log(
        self,
        player_tag: str,
    ) -> list[Battle]:
        return self._get(
            list[Battle],
            f"/players/{quote(player_tag, safe='#')}/battlelog",
        )

    def get_cards(
        self,
    ) -> CardList:
        return self._get(
            CardList,
            "/cards",
        )

    def get_tournaments(
        self,
        *,
        name: str | None = None,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[OutlinedTournament]:
        return self._get(
            PaginatedList[OutlinedTournament],
            "/tournaments",
            {
                "name": name,
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_tournament(
        self,
        tournament_tag: str,
    ) -> DetailedTournament:
        return self._get(
            DetailedTournament,
            f"/tournaments/{quote(tournament_tag, safe='#')}",
        )

    def get_current_clan_rankings(
        self,
        location_id: Literal["global"] | int = "global",
        *,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[RankedClan]:
        return self._get(
            PaginatedList[RankedClan],
            f"/locations/{quote(str(location_id), safe='')}/rankings/clans",
            {
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_current_clanwars_rankings(
        self,
        location_id: Literal["global"] | int = "global",
        *,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[RankedClan]:
        return self._get(
            PaginatedList[RankedClan],
            f"/locations/{quote(str(location_id), safe='')}/rankings/clanwars",
            {
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_seasonal_path_of_legends_rankings(
        self,
        season_id: str,
        *,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[RankedPlayer]:
        return self._get(
            PaginatedList[RankedPlayer],
            f"/locations/global/pathoflegend/{quote(season_id, safe='')}/rankings/players",
            {
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_seasonal_ladder_rankings(
        self,
        season_id: str,
        *,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[RankedPlayer]:
        return self._get(
            PaginatedList[RankedPlayer],
            f"/locations/global/seasons/{quote(season_id, safe='')}/rankings/players",
            {
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_seasons(
        self,
        *,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[Season]:
        return self._get(
            PaginatedList[Season],
            "/locations/global/seasons",
            {
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_locations(
        self,
        *,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[Location]:
        return self._get(
            PaginatedList[Location],
            "/locations",
            {
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_location(
        self,
        location_id: int,
    ) -> Location:
        return self._get(
            Location,
            f"/locations/{quote(str(location_id), safe='')}",
        )

    def get_global_tournament_rankings(
        self,
        tournament_tag: str,
        *,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[RankedTournamentPlayer]:
        return self._get(
            PaginatedList[RankedTournamentPlayer],
            f"/locations/global/rankings/tournaments/{quote(tournament_tag, safe='#')}",
            {
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_current_path_of_legends_rankings(
        self,
        location_id: Literal["global"] | int = "global",
        *,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[RankedPlayer]:
        return self._get(
            PaginatedList[RankedPlayer],
            f"/locations/{quote(str(location_id), safe='')}/pathoflegend/players",
            {
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_challenges(
        self,
    ) -> list[ChallengeChain]:
        return self._get(
            list[ChallengeChain],
            "/challenges",
        )

    def get_journey_leaderboard(
        self,
        journey_id: int,
        *,
        limit: int | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> PaginatedList[RankedJourneyLeaderboardPlayer]:
        return self._get(
            PaginatedList[RankedJourneyLeaderboardPlayer],
            f"/leaderboard/{quote(str(journey_id), safe='')}",
            {
                "limit": limit,
                "after": after,
                "before": before,
            },
        )

    def get_global_tournaments(
        self,
    ) -> ItemedList[GlobalTournament]:
        return self._get(
            ItemedList[GlobalTournament],
            "/globaltournaments",
        )

    def get_journey_leaderboards(
        self,
    ) -> ItemedList[JourneyLeaderboard]:
        return self._get(
            ItemedList[JourneyLeaderboard],
            "/leaderboards",
        )
