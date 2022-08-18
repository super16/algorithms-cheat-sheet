from abc import ABCMeta


class AbstractStrategy(metaclass=ABCMeta):

    """
    Abstract class for strategy.
    """

    @classmethod
    def __call__(self) -> str:
        return self.__name__


class AbstractContext(metaclass=ABCMeta):

    """
    Abstract class to create context for strategies.
    """

    @staticmethod
    def action(strategy_call: AbstractStrategy) -> str:
        """
        Call strategy.

        Args:
            strategy_call: Callable strategy class.
        """

        return strategy_call()
