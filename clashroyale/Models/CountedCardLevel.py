from pydantic.dataclasses import dataclass

from .UncountedCardLevel import UncountedCardLevel


@dataclass(kw_only=True)
class CountedCardLevel(UncountedCardLevel):
    count: int
