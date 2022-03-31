import abc
from typing import Dict


class BadParamsError(Exception):
    pass

class ExporterNotFoundError(Exception):
    pass

class UnknownError(Exception):
    pass


class ExporterT(abc.ABC):

    @abc.abstractmethod
    def send(self, msg: Dict):
        pass

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass


def get_by_name(name: str) -> ExporterT:
    return ExporterT()
