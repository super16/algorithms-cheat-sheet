from pytest import raises

from typing import Any, List, Tuple

from algorithms_cheat_sheet.search import Search


class TestSearch:

    """
    Tests for search classes.
    """

    search: Search = Search()

    search_attribs: Tuple[str, ...] = (
        "linear",
        "stdlib_binary",
    )

    correct_test_cases: Tuple[Tuple[List[int], int], ...] = (
        ([1, 2, 3], 1),
        ([1, 2, 3], 2),
        ([1, 2, 3], 3),
        ([1, 1, 1], 1),
        ([2, 2, 2], 2),
        ([3, 3, 4], 4),
        ([False, False, True], True),
        ([False, False, False], False),
    )

    incorrect_test_cases: Tuple[Tuple[List[int], int], ...] = (
        ([1, 2, 3], 4),
        ([1, 1, 1], 2),
        ([False, False, False], True),
    )

    wrong_inputs: Tuple[Any, ...] = (4.5, False, True, None)

    def test_approaches(self) -> None:
        """
        Test approaches for correct results.
        """
        for attrib in self.search_attribs:
            for test_case in self.correct_test_cases:
                assert getattr(
                    self.search,
                    attrib
                )(*test_case) == test_case[1]

    def test_nonexistent_value(self) -> None:
        """
        Test approaches for invalid results.
        """
        for attrib in self.search_attribs:
            for inccorrect_test_case in self.incorrect_test_cases:
                with raises(KeyError):
                    getattr(self.search, attrib)(*inccorrect_test_case)

    def test_noncollection(self) -> None:
        """
        Test wrong types of input (is not iterable).
        """
        for attrib in self.search_attribs:
            for wrong_input in self.wrong_inputs:
                with raises(TypeError):
                    getattr(self.search, attrib)(wrong_input, 1)
