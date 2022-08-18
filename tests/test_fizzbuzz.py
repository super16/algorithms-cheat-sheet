from pytest import CaptureFixture
from _pytest.capture import CaptureResult

from typing import Tuple

from algorithms_cheat_sheet.fizzbuzz import FizzBuzz


class TestFizzBuzz:

    """
    Tests for the FizzBuzz class.
    """

    fizzbuzz: FizzBuzz = FizzBuzz()

    fizzbuzz_approaches_attribs: Tuple[str, ...] = (
        "naive",
        "pattern_matching",
        "dry_code",
        "euler",
    )

    correct_answer: Tuple[str, ...] = (
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
        "16",
        "17",
        "Fizz",
        "19",
        "Buzz",
        "Fizz",
        "22",
        "23",
        "Fizz",
        "Buzz",
        "26",
        "Fizz",
        "28",
        "29",
        "FizzBuzz",
        "31",
        "32",
        "Fizz",
        "34",
        "Buzz",
        "Fizz",
        "37",
        "38",
        "Fizz",
        "Buzz",
        "41",
        "Fizz",
        "43",
        "44",
        "FizzBuzz",
        "46",
        "47",
        "Fizz",
        "49",
        "Buzz",
        "Fizz",
        "52",
        "53",
        "Fizz",
        "Buzz",
        "56",
        "Fizz",
        "58",
        "59",
        "FizzBuzz",
        "61",
        "62",
        "Fizz",
        "64",
        "Buzz",
        "Fizz",
        "67",
        "68",
        "Fizz",
        "Buzz",
        "71",
        "Fizz",
        "73",
        "74",
        "FizzBuzz",
        "76",
        "77",
        "Fizz",
        "79",
        "Buzz",
        "Fizz",
        "82",
        "83",
        "Fizz",
        "Buzz",
        "86",
        "Fizz",
        "88",
        "89",
        "FizzBuzz",
        "91",
        "92",
        "Fizz",
        "94",
        "Buzz",
        "Fizz",
        "97",
        "98",
        "Fizz",
        "Buzz",
    )

    def test_approaches(self, capfd: CaptureFixture) -> None:
        """
        Test correct approaches for results.
        """
        attrib: str
        for attrib in self.fizzbuzz_approaches_attribs:
            getattr(self.fizzbuzz, attrib)()
            output: CaptureResult = capfd.readouterr()
            assert output.out == "\n".join(self.correct_answer) + "\n"
