import unittest

from num_word_converter import num_to_word
from num_word_converter.errors import NonNumberInputError


class TestDigitToWord(unittest.TestCase):
    """
    Set of unit tests for testing the digit_to_word function.
    """

    def test_zero(self) -> None:
        """
        Test case for the number zero.
        """
        self.assertEqual(num_to_word(0), "zero")

    def test_unit_scale(self) -> None:
        """
        Test case for checking one-digit numbers.
        """
        self.assertEqual(num_to_word(1), "one")
        self.assertEqual(num_to_word(9), "nine")

    def test_two_digit_numbers(self) -> None:
        """
        Test case for checking two-digit numbers.
        """
        self.assertEqual(num_to_word(21), "twenty-one")
        self.assertEqual(num_to_word(99), "ninety-nine")

    def test_hundred_scale(self) -> None:
        """
        Test case for checking numbers in hundreds.
        """
        self.assertEqual(num_to_word(100), "one hundred")
        self.assertEqual(num_to_word(317), "three hundred and seventeen")

    def test_large_scale_numbers(self) -> None:
        """
        Test case for checking large scale numbers.
        """
        self.assertEqual(num_to_word(1000), "one thousand")
        self.assertEqual(num_to_word(5342), "five thousand three hundred and forty-two")
        self.assertEqual(num_to_word(800000), "eight hundred thousand")
        self.assertEqual(num_to_word(700800000), "seven hundred million eight hundred thousand")

    def test_negative_numbers(self) -> None:
        """
        Test case for negative numbers.
        """
        self.assertEqual(num_to_word(-1), "negative one")
        self.assertEqual(num_to_word(-999), "negative nine hundred and ninety-nine")

    def test_non_number_input(self) -> None:
        """
        Test case for checking non-numeric inputs.
        """
        with self.assertRaises(NonNumberInputError):
            num_to_word("Hello World")


if __name__ == '__main__':
    unittest.main()
