from pydantic.dataclasses import dataclass

from .Cursors import Cursors
from .Object import Object


@dataclass(frozen=True, kw_only=True)
class Paging(Object):
    cursors: Cursors
