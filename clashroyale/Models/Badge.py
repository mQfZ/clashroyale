from pydantic import HttpUrl
from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(kw_only=True)
class Badge(Object):
    name: str

    progress: int
    target: int | None = None

    level: int | None = None
    max_level: int | None = None

    icon_urls: dict[str, HttpUrl]
