import abc
from datetime import datetime


class RuleT(abc.ABC):

    @property
    @abc.abstractmethod
    def id(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass


class ScheduleT(abc.ABC):

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
    def timestamp(self) -> datetime:
        pass


class ContextT(abc.ABC):

    @property
    @abc.abstractmethod
    def msg(self) -> MessageT:
        pass

    @property
    @abc.abstractmethod
    def rule(self) -> RuleT:
        pass

    @property
    @abc.abstractmethod
    def schedule(self) -> ScheduleT:
        pass


def current() -> ContextT:
    pass
