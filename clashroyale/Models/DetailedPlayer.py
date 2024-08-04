from pydantic import Field
from pydantic.dataclasses import dataclass

from .Achievement import Achievement
from .Badge import Badge
from .Journey import Journey
from .CountedLeveledPlayingCard import CountedLeveledPlayingCard
from .CountedLeveledSupportingCard import CountedLeveledSupportingCard
from .OutlinedPlayer import OutlinedPlayer
from .PathOfLegendResult import PathOfLegendResult
from .PlayerLeagueStatistics import PlayerLeagueStatistics
from .LevellessPlayingCard import LevellessPlayingCard


@dataclass(kw_only=True)
class DetailedPlayer(OutlinedPlayer):
    best_trophies: int
    journeys: dict[str, Journey] = Field(alias="progress")
    league_statistics: PlayerLeagueStatistics | None = None
    legacy_trophy_road_high_score: int | None
    current_path_of_legend_season_result: PathOfLegendResult | None
    last_path_of_legend_season_result: PathOfLegendResult | None
    best_path_of_legend_season_result: PathOfLegendResult | None

    achievements: list[Achievement]
    badges: list[Badge]
    star_points: int
    exp_points: int
    total_exp_points: int
    playing_cards: list[CountedLeveledPlayingCard] = Field(alias="cards")
    supporting_cards: list[CountedLeveledSupportingCard] = Field(alias="supportCards")
    current_deck_playing_cards: list[CountedLeveledPlayingCard] = Field(alias="currentDeck")
    current_deck_supporting_cards: list[CountedLeveledSupportingCard] = Field(alias="currentDeckSupportCards")
    current_favourite_card: LevellessPlayingCard | None = None

    battle_count: int
    wins: int
    losses: int
    three_crown_wins: int

    challenge_max_wins: int
    challenge_cards_won: int
    tournament_battle_count: int
    tournament_cards_won: int

    total_donations: int
    war_day_wins: int
    clan_cards_collected: int
