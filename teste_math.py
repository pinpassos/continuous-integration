import unittest

from my_math import sum_numbers


class MyMathTestCase(unittest.TestCase):
    """Test case for the sum_numbers function."""

    def test_addition_sum_number(self):
        """Test the sum of two numbers."""
        sum_numbers_result = sum_numbers(5, 5)
        self.assertEqual(sum_numbers_result, 120)


if __name__ == '__main__':
    unittest.main()
