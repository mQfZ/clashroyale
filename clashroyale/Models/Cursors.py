from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(frozen=True, kw_only=True)
class Cursors(Object):
    before: str | None = None
    after: str | None = None
