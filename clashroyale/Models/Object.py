from pydantic.alias_generators import to_camel
from pydantic.config import ConfigDict
from pydantic.dataclasses import dataclass


@dataclass(config=ConfigDict(alias_generator=to_camel), kw_only=True)
class Object:
    pass
