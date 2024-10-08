from pydantic.dataclasses import dataclass

from .TaggedClan import TaggedClan


@dataclass(frozen=True, kw_only=True)
class BadgedClan(TaggedClan):
    name: str
    badge_id: int
