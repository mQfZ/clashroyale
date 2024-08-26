from pydantic.dataclasses import dataclass

from .UncountedCardLevel import UncountedCardLevel


@dataclass(frozen=True, kw_only=True)
class CountedCardLevel(UncountedCardLevel):
    count: int
