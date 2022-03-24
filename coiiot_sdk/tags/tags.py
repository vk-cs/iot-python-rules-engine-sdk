from typing import Iterator
from ..context import TagT, TagTypeEnum

class TagNotFoundError(Exception):
    pass

class BadParamsError(Exception):
    pass

class UnknownError(Exception):
    pass

def get(tag_id: int) -> TagT:
    pass

def root() -> TagT:
    pass

def get_child_by_name(tag_id: int, child_name: str) -> TagT:
    pass

def select_by_type(tag_type: TagTypeEnum) -> Iterator[TagT]:
    pass
