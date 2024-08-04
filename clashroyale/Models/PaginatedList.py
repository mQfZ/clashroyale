from pydantic.dataclasses import dataclass

from .ItemedList import ItemedList
from .Paging import Paging


@dataclass(kw_only=True)
class PaginatedList[T](ItemedList[T]):
    paging: Paging
