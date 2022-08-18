from abc import ABCMeta, abstractmethod


class AbstractProduct(metaclass=ABCMeta):

    """
    Abstract product class.
    """

    def __init__(self, title: str) -> None:
        self.title = title

    def __str__(self) -> str:
        return self.title


class AbstractFactory(metaclass=ABCMeta):

    """
    Abstract factory pattern class.
    """

    @abstractmethod
    def create_product(self) -> AbstractProduct:  # pragma: no cover
        """
        Product creation method.

        Args:
            product (AbstractProduct): product to create.
        """
        pass
