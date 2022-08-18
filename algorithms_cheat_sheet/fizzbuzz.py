from typing import Dict


class FizzBuzz:

    """
    Function to print the integers from 1 to 100,
    but for every multiple of 3, write “Fizz”,
    and for every multiple of 5, write “Buzz”.
    For numbers which are multiples of both 3 and 5,
    it should write “FizzBuzz”;
    for every other number,
    it should print the number unchanged.
    """

    def __init__(self) -> None:
        self.start_number: int = 1
        self.end_number: int = 100

        # For Euler's approach
        self.eulers_dict: Dict[int, str] = {
            0: "FizzBuzz",
            6: "Fizz",
            10: "Buzz",
        }

    def naive(self) -> None:
        """
        Naive approach.

        Returns:
            Prints out FizzBuzz sequence.
        """

        number: int
        for number in range(self.start_number, self.end_number + 1):
            if number % 15 == 0:
                print("FizzBuzz")
            elif number % 3 == 0:
                print("Fizz")
            elif number % 5 == 0:
                print("Buzz")
            else:
                print(number)

    def pattern_matching(self) -> None:
        """
        Naive approach using match/case syntax
        (works since Python 3.10, PEP 634).

        Returns:
            Prints out FizzBuzz sequence.
        """

        number: int
        for number in range(self.start_number, self.end_number + 1):
            match number:
                case _ if number % 15 == 0:
                    print("FizzBuzz")
                case _ if number % 3 == 0:
                    print("Fizz")
                case _ if number % 5 == 0:
                    print("Buzz")
                case _:
                    print(number)

    def dry_code(self) -> None:
        """
        DRY code approach to avoid excessive
        condition statements. (from rosettacode.org)

        Returns:
            Prints out FizzBuzz sequence.
        """

        number: int
        for number in range(self.start_number, self.end_number + 1):
            response: str = ""

            if not number % 3:
                response += "Fizz"
            if not number % 5:
                response += "Buzz"

            print(response or number)

    def euler(self) -> None:
        """
        Overengineering approach with Euler's theorem.
        Taken from http://philcrissman.net/posts/eulers-fizzbuzz/

        Returns:
            Prints out FizzBuzz sequence.
        """

        number: int
        for number in range(self.start_number, self.end_number + 1):
            print(self.eulers_dict.get(number ** 4 % 15) or number)
