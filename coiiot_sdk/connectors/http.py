import abc
from typing import Dict, Union, Any


Headers = Dict[str, str]
Params = Dict[str, str]


class BadParamsError(Exception):
    pass

class ConnectorNotFoundError(Exception):
    pass

class UnknownError(Exception):
    pass

class NonHTTPConnectorError(Exception):
    pass

class HTTPResponseT(abc.ABC):

    @property
    @abc.abstractmethod
    def status_code(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def headers(self) -> Headers:
        pass

    @property
    @abc.abstractmethod
    def text(self) -> str:
        pass

    @abc.abstractmethod
    def json(self) -> Any:
        pass


class HTTPConnectorT(abc.ABC):

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @abc.abstractmethod
    def get(self,
            path: Union[str, None] = None,
            params: Union[Params, None] = None,
            headers: Union[Headers, None] = None) -> HTTPResponseT:

        pass

    @abc.abstractmethod
    def post(self,
             path: Union[str, None] = None,
             data: Union[Any, None] = None,
             headers: Union[Headers, None] = None) -> HTTPResponseT:

        pass

    @abc.abstractmethod
    def put(self,
            path: Union[str, None] = None,
            data: Union[Any, None] = None,
            headers: Union[Headers, None] = None) -> HTTPResponseT:

        pass

    @abc.abstractmethod
    def patch(self,
              path: Union[str, None] = None,
              data: Union[Any, None] = None,
              headers: Union[Headers, None] = None) -> HTTPResponseT:

        pass

    @abc.abstractmethod
    def delete(self,
               path: Union[str, None] = None,
               headers: Union[Headers, None] = None) -> HTTPResponseT:

        pass


def get_http_connector(name: str) -> HTTPConnectorT:
    return HTTPConnectorT()
