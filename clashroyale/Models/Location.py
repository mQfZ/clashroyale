from pydantic.dataclasses import dataclass

from .Object import Object


@dataclass(kw_only=True)
class Location(Object):
    id: int
    name: str

    is_country: bool
    country_code: str | None = None
