from bisect import bisect_left
from collections.abc import Sequence
from functools import wraps
from typing import Any, Callable, TypeVar


SType = TypeVar("SType", bound="Search")
SearchCallable = Callable[[SType, Sequence, Any], Any]


class Search:

    """
    Search algorithms class.
    """

    def __init__(self) -> None:
        """
        Search constructor.
        """
        pass

    @staticmethod
    def validate_collection(func: SearchCallable) -> SearchCallable:
        """
        Decorator to validate that collection is a sequence object.

        Raises:
            TypeError: An input collection isn't a sequence object.
        """

        @wraps(func)
        def validator_wrapper(
            self, input_collection: Sequence, item: Any
        ) -> SearchCallable:

            if not isinstance(input_collection, Sequence):
                raise TypeError("Input collection should be a sequence")

            return func(self, input_collection, item)

        return validator_wrapper

    @validate_collection
    def linear(self, input_collection: Sequence, item: Any) -> Any:
        """
        Basic linear search.

        Args:
            input_collection (Sequence): collection of items.
            item (Any): item to find among collection.

        Returns:
            Found item.

        Raises:
            KeyError: Item doesn't exist in input collection.
        """

        collection_element: Any
        for collection_element in input_collection:
            if collection_element == item:
                return collection_element
        raise KeyError("Item doesn\'t exists")

    @validate_collection
    def stdlib_binary(self, input_collection: Sequence, item: Any) -> Any:
        """
        Binary search using bisect_left from bisect standard module.

        Args:
            input_collection (Sequence): collection of items.
            item (Any): item to find among collection.

        Returns:
            Found item.

        Raises:
            KeyError: Item doesn't exist in input collection.
        """

        idx: int = bisect_left(input_collection, item)
        if idx != len(input_collection) and input_collection[idx] == item:
            return input_collection[idx]
        raise KeyError("Item doesn\'t exists")
