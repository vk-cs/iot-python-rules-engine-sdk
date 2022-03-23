import abc
from typing import Any, List, Dict, NamedTuple, Optional, TypedDict
import datetime

from ..context import TagT
from ..context import TagTypeEnum, ValueTypeEnum


class NoDeviceFoundError(Exception):
    pass

class NoAgentFoundError(Exception):
    pass

class BadParamsError(Exception):
    pass

class UnknownError(Exception):
    pass



class Driver(abc.ABC):

    @property
    @abc.abstractmethod
    def id(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass


class DeviceAgentType(abc.ABC):

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
    def label(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def drivers(self) -> List[Driver]:
        pass


class DeviceAgent(abc.ABC):

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
    def label(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def type(self) -> DeviceAgentType:
        pass


class DeviceType(abc.ABC):

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
    def label(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def driver(self) -> Driver:
        pass



class Device(abc.ABC):

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
    def label(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def type(self) -> DeviceType:
        pass

    @property
    @abc.abstractmethod
    def tag(self) -> TagT:
        pass

    @property
    @abc.abstractmethod
    def first_seen_at(self) -> int:
        pass
    
    @property
    @abc.abstractmethod
    def last_seen_at(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def agent(self) -> Optional[DeviceAgent]:
        pass


class AgentType(abc.ABC):

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
    def label(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def drivers(self) -> List[Driver]:
        pass


class AgentDevice(abc.ABC):

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
    def label(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def type(self) -> DeviceType:
        pass



class Agent(abc.ABC):

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
    def label(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def first_seen_at(self) -> int:
        pass
    
    @property
    @abc.abstractmethod
    def last_seen_at(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def type(self) -> AgentType:
        pass

    @property
    @abc.abstractmethod
    def tag(self) -> TagT:
        pass

    @property
    @abc.abstractmethod
    def devices(self) -> List[AgentDevice]:
        pass


class State(TypedDict):
    received_at: int
    state_changed: bool
    tag_id: int
    timestamp: int
    value: Any


class ChangedStates(TypedDict):
    states: List[State]


class UpdateT(abc.ABC):

    @abc.abstractmethod
    def change_state(self, tag: TagT, new_value: Any) -> 'UpdateT':
        pass

    @abc.abstractmethod
    def execute(self) -> ChangedStates:
        pass


def change_state(tag: TagT, new_value: Any) -> UpdateT:
    return UpdateT()


def get_agent_by_id(agent_id: int) -> Agent:
    pass


def get_device_by_id(device_id: int) -> Device:
    pass