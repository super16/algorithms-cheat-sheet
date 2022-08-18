from pytest import raises

from typing import Any, Dict, Tuple

from algorithms_cheat_sheet.fibonacci import FibonacciNumber


class TestFibonacciNumber:

    """
    Tests for the FibonacciNumber class.
    """

    fibonacci_number: FibonacciNumber = FibonacciNumber()

    fibonacci_number_attribs: Tuple[str, ...] = (
        'recursive',
        'memoization',
        'cache_memoization',
        'iterative',
        'generator',
    )

    correct_results: Dict[int, int] = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 3,
        5: 5,
        6: 8,
        7: 13,
        8: 21,
        9: 34,
        10: 55,
        11: 89,
        12: 144,
        13: 233,
        14: 377,
        15: 610,
        16: 987,
        17: 1597,
        18: 2584,
        19: 4181,
        20: 6765,
    }

    wrong_inputs: Tuple[Any, ...] = (
        (1, 2, 3),
        [1, 2, 3],
        {"foo": "bar", 1: 2},
        4.5,
        False,
        True,
        None,
        "Foo",
    )

    negative_input: int = -1

    def test_approaches(self) -> None:
        """
        Test correct approaches for results.
        """
        for attrib in self.fibonacci_number_attribs:
            for number, result in self.correct_results.items():
                assert getattr(
                    self.fibonacci_number,
                    attrib
                )(number) == result

    def test_wrong_inputs(self) -> None:
        """
        Test wrong types of input.
        """
        for wrong_input in self.wrong_inputs:
            for attrib in self.fibonacci_number_attribs:
                if (attrib == "cache_memoization"):
                    self.fibonacci_number.cache_memoization.cache_clear()
                with raises(TypeError):
                    getattr(self.fibonacci_number, attrib)(wrong_input)

    def test_negative_input(self) -> None:
        """
        Test for negative integer input_number.
        """
        for attrib in self.fibonacci_number_attribs:
            with raises(ValueError):
                getattr(self.fibonacci_number, attrib)(self.negative_input)
