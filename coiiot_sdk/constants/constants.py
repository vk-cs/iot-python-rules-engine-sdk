import abc
from typing import Any
from enum import Enum, unique


class BadParamsError(Exception):
    pass

class ConstantNotFoundError(Exception):
    pass

class UnknownError(Exception):
    pass


@unique
class Type(Enum):
    int = 0
    float = 1
    long = 2
    double = 3
    timestamp = 4
    string = 5
    array = 6


class ConstantT(abc.ABC):

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
    def type(self) -> Type:
        pass

    @property
    @abc.abstractmethod
    def value(self) -> Any:
        pass


def get_by_name(name: str) -> ConstantT:
    return ConstantT()
