import unittest

from num_word_converter import word_to_num
from num_word_converter.errors import NoConversionForWordError, ScaleOutOfOrderError


class TestConvertToDigit(unittest.TestCase):
    """
    Set of unit tests for testing the convert_to_digit function.
    """

    def test_zero_case(self) -> None:
        """
        Test case for checking if the number zero is converted correctly.
        """
        self.assertEqual(word_to_num('zero'), 0)

    def test_case_sensitivity(self) -> None:
        """
        Test case for checking the case-insensitivity of the function.
        """
        self.assertEqual(word_to_num('One'), 1)
        self.assertEqual(word_to_num('ONE'), 1)

    def test_spacing(self) -> None:
        """
        Test case for invalid spacing in the input string.
        """
        self.assertEqual(word_to_num('  one '), 1)
        self.assertEqual(word_to_num('twenty   one'), 21)

    def test_decimal_numbers(self) -> None:
        """
        Test case for decimal numbers. Checking if the function properly converts decimal numbers.
        """
        self.assertEqual(word_to_num('one point five'), 1.5)
        self.assertEqual(word_to_num('zero point nine'), 0.9)

    def test_large_scaled_numbers(self) -> None:
        """
        Test case for large scaled numbers. Checking if the function correctly converts large scale numbers like trillion.
        """
        self.assertEqual(word_to_num('one trillion'), 1000000000000)
        self.assertEqual(word_to_num('five thousand three hundred and forty-two'), 5342)

    def test_mixed_case_numbers(self) -> None:
        """
        Test case for mixed case numbers. Checking if the function properly converts the numbers regardless of the case.
        """
        self.assertEqual(word_to_num('Two Hundred ThREe'), 203)
        self.assertEqual(word_to_num('four point ninE'), 4.9)

    def test_error_cases(self) -> None:
        """
        Test cases for expected error scenarios. Checking if the function correctly raises the appropriate errors.
        """
        with self.assertRaises(NoConversionForWordError):
            word_to_num('invalid input')
        with self.assertRaises(ScaleOutOfOrderError):
            word_to_num('one thousand hundred')


if __name__ == '__main__':
    unittest.main()
