from functools import lru_cache, wraps
from typing import Callable, Dict, Generator, TypeVar


FType = TypeVar("FType", bound="FibonacciNumber")
FibNumberCallable = Callable[[FType, int], int]


class FibonacciNumber:

    """
    The Fibonacci numbers form a sequence, the Fibonacci sequence,
    in which each number is the sum of the two preceding ones.
    The sequence commonly starts from 0 and 1.
    """

    def __init__(self) -> None:
        """
        Fibonacci constructor.
        """
        self.memory: Dict[int, int] = {0: 0, 1: 1}

    @staticmethod
    def validate_input(func: FibNumberCallable) -> FibNumberCallable:
        """
        Decorator to validate input number for the following approaches.

        Raises:
            TypeError: An input number is not integer.
            ValueError: An input number is negative integer.
        """

        @wraps(func)
        def validator_wrapper(self, input_number: int):
            if not type(input_number) is int:
                raise TypeError(
                    f"input_number for {self.__class__.__name__} "
                    "should be integer"
                )

            if type(input_number) is int and input_number < 0:
                raise ValueError("input_number should be a positive integer")

            return func(self, input_number)

        return validator_wrapper

    @validate_input
    def recursive(self, input_number: int) -> int:
        """
        Recursive approach. Don't try over 30.

        Args:
            input_number (int): Index of Fibonacci
            numbers sequence.

        Returns:
            Calculated Fibonacci number.
        """

        if input_number < 2:
            return input_number

        return self.recursive(input_number - 2) \
            + self.recursive(input_number - 1)

    @validate_input
    def memoization(self, input_number: int) -> int:
        """
        Memoization approach using self.memory dictionary
        to store values.

        Args:
            input_number (int): Index of Fibonacci
            numbers sequence.

        Returns:
            Calculated Fibonacci number.
        """

        if input_number not in self.memory:
            self.memory[input_number] = \
                self.memoization(input_number - 2) \
                + self.memoization(input_number - 1)
        return self.memory[input_number]

    @lru_cache(maxsize=None, typed=False)
    @validate_input
    def cache_memoization(self, input_number: int) -> int:
        """
        Memoization approach using least recently used (lru)
        cache decorator.

        Args:
            input_number (int): Index of Fibonacci
            numbers sequence.

        Returns:
            Calculated Fibonacci number.
        """

        if input_number < 2:
            return input_number

        return self.cache_memoization(input_number - 2) \
            + self.cache_memoization(input_number - 1)

    @validate_input
    def iterative(self, input_number: int) -> int:
        """
        Iterative approach.

        Args:
            input_number (int): Index of Fibonacci
            numbers sequence.

        Returns:
            Calculated Fibonacci number.
        """

        if input_number == 0:
            return input_number
        last_number: int = 0
        next_number: int = 1
        for _ in range(1, input_number):
            last_number, next_number = next_number, last_number \
                + next_number
        return next_number

    def _generator(self) -> Generator[int, None, None]:
        """
        Fibonacci generator.

        Yields:
            int: Current calculated Fibonacci number.
        """
        last_number: int = 0
        next_number: int = 1
        while True:
            yield last_number
            last_number, next_number = next_number, last_number \
                + next_number

    @validate_input
    def generator(self, input_number: int) -> int:
        """
        Generator approach.

        Args:
            input_number (int): Index of Fibonacci
            numbers sequence.

        Returns:
            Calculated Fibonacci number.
        """

        value: int = 0
        fn_generator: Generator[int, None, None] = self._generator()
        for _ in range(input_number + 1):
            value = next(fn_generator)
        return value
