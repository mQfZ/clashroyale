from pydantic.dataclasses import dataclass

from .NamedChest import NamedChest


@dataclass(kw_only=True)
class IndexedChest(NamedChest):
    index: int
