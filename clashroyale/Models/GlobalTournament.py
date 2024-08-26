from pydantic import Field
from pydantic.dataclasses import dataclass

from .IDedGameMode import IDedGameMode
from .DateTime import DateTime
from .Object import Object
from .Reward import Reward


@dataclass(frozen=True, kw_only=True)
class GlobalTournament(Object):
    tag: str
    name: str = Field(alias="title")

    start_time: DateTime
    end_time: DateTime
    game_mode: IDedGameMode
    max_losses: int
    min_exp_level: int
    tournament_level: int

    paid_rewards: list[Reward] = Field(alias="milestoneRewards")
    free_rewards: list[Reward] = Field(alias="freeTierRewards")
    top_rank_reward: list[Reward]
    max_top_reward_rank: int
