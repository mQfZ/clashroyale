from pydantic.dataclasses import dataclass

from clashroyale.Models.ItemedList import ItemedList
from clashroyale.Models.Paging import Paging


@dataclass(frozen=True, kw_only=True)
class PaginatedList[T](ItemedList[T]):
    items: list[T]
    paging: Paging
