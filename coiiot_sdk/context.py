import abc
from typing import Any, Dict, List, Optional, NamedTuple
from enum import Enum, unique
from datetime import datetime


class TagNotFoundError(Exception):
    pass

class UnknownError(Exception):
    pass


@unique
class TagTypeEnum(Enum):
    undefined = 0
    event = 1
    state = 2
    node = 3
    device = 4
    agent = 5
    aggregate = 6


@unique
class ValueTypeEnum(Enum):
    integer = 1
    float = 2
    boolean = 3
    string = 4
    location = 5
    timestamp = 6


class TagStateT(abc.ABC):

    @property
    @abc.abstractmethod
    def received_at(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def timestamp(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def value(self) -> Any:
        pass


class TagT(abc.ABC):

    @property
    @abc.abstractmethod
    def id(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def full_name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def type(self) -> TagTypeEnum:
        pass

    @property
    @abc.abstractmethod
    def attrs(self) -> Dict[str, str]:
        pass

    @property
    @abc.abstractmethod
    def children(self) -> List['TagT']:
        pass

    @property
    @abc.abstractmethod
    def parent(self) -> Optional['TagT']:
        pass

    @property
    @abc.abstractmethod
    def value_type(self) -> Optional[ValueTypeEnum]:
        pass

    @property
    @abc.abstractmethod
    def state(self) -> Optional[TagStateT]:
        pass

    @abc.abstractmethod
    def get_child(self, name: str) -> Optional['TagT']:
        pass


class RuleT(abc.ABC):

    @property
    @abc.abstractmethod
    def id(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass


class MessageT(abc.ABC):

    @property
    @abc.abstractmethod
    def type(self) -> ValueTypeEnum:
        pass

    @property
    @abc.abstractmethod
    def value(self) -> Any:
        pass

    @property
    @abc.abstractmethod
    def timestamp(self) -> datetime:
        pass


class ContextT(abc.ABC):

    @property
    @abc.abstractmethod
    def tag(self) -> TagT:
        pass

    @property
    @abc.abstractmethod
    def root_tag(self) -> TagT:
        pass

    @property
    @abc.abstractmethod
    def msg(self) -> MessageT:
        pass

    @property
    @abc.abstractmethod
    def rule(self) -> RuleT:
        pass


def current() -> ContextT:
    pass
