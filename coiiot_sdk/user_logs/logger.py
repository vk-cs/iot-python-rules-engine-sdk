import abc


class LoggerT(abc.ABC):

    @abc.abstractmethod
    def error(self, msg: str):
        pass

    @abc.abstractmethod
    def info(self, msg: str):
        pass


def get_logger() -> LoggerT:
    return LoggerT()
