import abc
from typing import Any, Dict, Union, List, TypedDict
from datetime import datetime

from ..context import MessageT, TagT


class HttpError(Exception):
    pass


class InsertionError(Exception):
    pass


class UpsertionError(Exception):
    pass


class SelectionError(Exception):
    pass


class BadParamsError(Exception):
    pass


class NotFoundError(Exception):
    pass


class InsertT(abc.ABC):

    @abc.abstractmethod
    def values(self, tag_id: int, value: Any, timestamp: datetime) -> 'InsertT':
        pass

    @abc.abstractmethod
    def msg(self, msg: MessageT) -> 'InsertT':
        pass

    @abc.abstractmethod
    def execute(self):
        pass


def insert() -> InsertT:
    return InsertT()


class UpsertT(abc.ABC):

    @abc.abstractmethod
    def values(self, tag_id: int, value: Any, timestamp: datetime) -> 'UpsertT':
        pass

    @abc.abstractmethod
    def msg(self, msg: MessageT) -> 'UpsertT':
        pass

    @abc.abstractmethod
    def execute(self):
        pass


def upsert() -> UpsertT:
    return UpsertT()


class Event(TypedDict):
    payload: Dict[str, Any]
    received_at: int
    time: int
    value: Any


class LatestEvent(TypedDict):
    data: Event
    tag_id: int
    value_type: str


class Events(TypedDict):
    data: List[Event]
    tag_id: int
    value_type: str


class EventsAggregate(TypedDict):
    data: Dict[str, Union[int, float]]
    tag_id: int
    value_type: str


class GroupAggregateOfEvents(TypedDict):
    end_time: int
    start_time: int
    value: Dict[str, Union[int, float]]


class EventsGroupAggregate(TypedDict):
    data: List[GroupAggregateOfEvents]
    tag_id: int
    value_type: str


class Aggregate(TypedDict):
    payload: Dict[str, Any]
    received_at: int
    time: int
    value: Any


class CurrentAggregate(TypedDict):
    data: Aggregate
    tag_id: int
    value_type: str


class Aggregates(TypedDict):
    data: List[Aggregate]
    tag_id: int
    value_type: str


class AggregatesAggregate(TypedDict):
    data: Dict[str, Union[int, float]]
    tag_id: int
    value_type: str


class GroupAggregateOfAggregates(TypedDict):
    end_time: int
    start_time: int
    value: Dict[str, Union[int, float]]


class AggregatesGroupAggregate(TypedDict):
    data: List[GroupAggregateOfAggregates]
    tag_id: int
    value_type: str


AggregateEvents = Union[EventsAggregate, EventsGroupAggregate]
EventsResult = Union[AggregateEvents, Events]

AggregateAggregates = Union[AggregatesAggregate, AggregatesGroupAggregate]
AggregatesResult = Union[AggregateAggregates, Aggregates]

SelectionResult = Union[AggregatesResult, EventsResult]


class SelectT(abc.ABC):

    @abc.abstractmethod
    def with_offset(self, offset: int) -> 'SelectT':
        pass

    @abc.abstractmethod
    def with_limit(self, limit: int) -> 'SelectT':
        pass

    @abc.abstractmethod
    def with_period(self, period: str) -> 'SelectT':
        pass

    @abc.abstractmethod
    def calc_max_as(self, alias: str) -> 'SelectT':
        pass

    @abc.abstractmethod
    def calc_max(self) -> 'SelectT':
        pass

    @abc.abstractmethod
    def calc_avg_as(self, alias: str) -> 'SelectT':
        pass

    @abc.abstractmethod
    def calc_avg(self) -> 'SelectT':
        pass

    @abc.abstractmethod
    def calc_count_as(self, alias: str) -> 'SelectT':
        pass

    @abc.abstractmethod
    def calc_count(self) -> 'SelectT':
        pass

    @abc.abstractmethod
    def calc_sum_as(self, alias: str) -> 'SelectT':
        pass

    @abc.abstractmethod
    def calc_sum(self) -> 'SelectT':
        pass

    @abc.abstractmethod
    def calc_min_as(self, alias: str) -> 'SelectT':
        pass

    @abc.abstractmethod
    def calc_min(self) -> 'SelectT':
        pass

    @abc.abstractmethod
    def order_by(self, **kwargs) -> 'SelectT':
        pass

    @abc.abstractmethod
    def execute(self) -> SelectionResult:
        pass


def select(tag: TagT, from_ts: datetime, to_ts: datetime) -> SelectT:
    return SelectT()


class SelectLatestT(abc.ABC):

    @abc.abstractmethod
    def execute(self) -> LatestEvent:
        pass

def select_latest(tag: TagT) -> SelectLatestT:
    return SelectLatestT()


class SelectCurrentT(abc.ABC):

    @abc.abstractmethod
    def execute(self) -> CurrentAggregate:
        pass

def select_current(tag: TagT) -> SelectCurrentT:
    return SelectCurrentT()
