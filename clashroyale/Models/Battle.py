from pydantic.dataclasses import dataclass

from .Arena import Arena
from .BattlePlayer import BattlePlayer
from .DateTime import DateTime
from .NamedGameMode import NamedGameMode
from .Object import Object


@dataclass(kw_only=True)
class Battle(Object):
    type: str
    battle_time: DateTime
    arena: Arena
    league_number: int
    game_mode: NamedGameMode
    deck_selection: str

    team: list[BattlePlayer]
    opponent: list[BattlePlayer]

    is_hosted_match: bool
    is_ladder_tournament: bool

    tournament_tag: str | None = None
    challenge_title: str | None = None
    challenge_id: int | None = None
    challenge_win_count_before: int | None = None

    boat_battle_side: str | None = None
    boat_battle_won: bool | None = None
    new_towers_destroyed: int | None = None
    prev_towers_destroyed: int | None = None
    remaining_towers: int | None = None
