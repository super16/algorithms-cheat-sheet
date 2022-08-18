from abc import ABCMeta, abstractmethod
from base64 import b64encode
from functools import wraps
from typing import Any, Callable, Optional, TypeVar


ProxyType = TypeVar("ProxyType", bound="Proxy")
ProxyCallable = Callable[[ProxyType], bytes | None]


class AbstractSubject(metaclass=ABCMeta):

    """
    Abstract base class for Subject, RealSubject and its proxy.
    """

    @abstractmethod
    def expensive_action(self) -> Any:  # pragma: no cover
        """
        Abstract method for expensive operation.
        """
        pass

    @abstractmethod
    def data(self) -> Any:  # pragma: no cover
        """
        Abstract method to get expensive data.
        """
        pass


class RealSubject(AbstractSubject):

    """
    Class that should be controlled by Proxy class.
    """

    def __init__(self, title: str) -> None:
        """
        Part constructor.

        Args:
            title (str): Title to object.
        """
        self._data: Optional[bytes] = None
        self.title: str = title

    def expensive_action(self) -> None:
        """
        Example of expensive operation with object as encoding
        title to base64.
        """
        self._data = b64encode(self.title.encode())

    def data(self) -> Optional[bytes]:
        """
        Getter to data property.

        Returns:
            Encoded to base64 object title or None.
        """

        return self._data


class Proxy(AbstractSubject):

    """
    Proxy class to control creating and access to RealSubject.
    RealSubject is not created during initializing Proxy, but
    with any method calling.
    """

    def __init__(self, subject_title: str) -> None:
        self._real_subject: Optional[RealSubject] = None
        self.subject_title: str = subject_title

    @staticmethod
    def create_real_subject_lazily(func: ProxyCallable) -> ProxyCallable:
        @wraps(func)
        def real_subject_creator(self: ProxyType):
            if not self._real_subject:
                self._real_subject = RealSubject(title=self.subject_title)

            return func(self)

        return real_subject_creator

    @create_real_subject_lazily
    def expensive_action(self) -> None:
        if self._real_subject:
            self._real_subject.expensive_action()

    @create_real_subject_lazily
    def data(self) -> Optional[bytes]:
        if self._real_subject is not None:
            return self._real_subject.data()
        else:  # pragma: no cover
            return None
