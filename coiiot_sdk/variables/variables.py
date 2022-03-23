import abc
from typing import Any, NamedTuple
from enum import Enum, unique
from datetime import datetime


class BadParamsError(Exception):
    pass

class VariableNotFoundError(Exception):
    pass

class UnknownError(Exception):
    pass


@unique
class Types(str, Enum):
    Integer = "integer"
    Float = "float"
    Timestamp = "timestamp"
    String = "string"
    Boolean = "boolean"
    Location = "location"


class Location(NamedTuple):
    lat: float
    lng: float


class VariableT(abc.ABC):

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def value_type(self) -> Types:
        pass

    @property
    @abc.abstractmethod
    def value(self) -> Any:
        pass

    @property
    @abc.abstractmethod
    def timestamp(self) -> datetime:
        pass

    @property
    @abc.abstractmethod
    def expires_at(self) -> datetime:
        pass

    @abc.abstractmethod
    def set(self, value: Any, timestamp: datetime, ttl=None, create=False, force=False) -> 'VariableT':
        pass

    @abc.abstractmethod
    def increment(self, delta: Any, ttl=None, default_value=0, create=False) -> 'VariableT':
        pass

    @abc.abstractmethod
    def decrement(self, delta: Any, ttl=None, default_value=0, create=False) -> 'VariableT':
        pass

    @abc.abstractmethod
    def delete(self):
        pass

    @abc.abstractmethod
    def exists(self) -> bool:
        pass


def get(name: str) -> VariableT:
    return VariableT()


def create(name: str, value: Any, value_type: Types, timestamp: datetime, ttl: int) -> VariableT:
    return VariableT()


def set(name: str, value: Any, value_type: Types, create: bool, force: bool, timestamp: datetime, ttl: int) -> VariableT:
    return VariableT()


def increment(name: str, delta: Any, value_type: Types, ttl=None, default_value=0, create=False) -> VariableT:
    return VariableT()


def decrement(name: str, delta: Any, value_type: Types, ttl=None, default_value=0, create=False) -> VariableT:
    return VariableT()


def delete(name: str):
    pass


def exists(name: str) -> bool:
    pass