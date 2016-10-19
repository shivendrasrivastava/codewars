__author__ = "Shiven"

import unittest
from io import StringIO
from unittest.mock import patch
from calculate_multiples import calculate


class TestCalculateMultiples(unittest.TestCase):

    simple_input_1 = iter(["100","2", "4"]).__next__

    @patch("builtins.input", simple_input_1)
    def test_calculate_multiples_1(self):
        out = StringIO()
        with patch("sys.stdout", out) as output:
            calculate()
        output = output.getvalue().strip()
        self.assertEqual(output, "Fizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz\nFizz\nFizzBuzz")

    simple_input_2 = iter(["100", "3", "5"]).__next__

    @patch("builtins.input", simple_input_2)
    def test_calculate_multiples_2(self):
        out = StringIO()
        with patch("sys.stdout", out) as output:
            calculate()
        output = output.getvalue().strip()
        self.assertEqual(output, "Fizz\nBuzz\nFizz\nFizz\nBuzz\nFizz\nFizzBuzz\nFizz\nBuzz\nFizz\nFizz\nBuzz\nFizz\nFizzBuzz\nFizz\nBuzz\nFizz\nFizz\nBuzz\nFizz\nFizzBuzz\nFizz\nBuzz\nFizz\nFizz\nBuzz\nFizz\nFizzBuzz\nFizz\nBuzz\nFizz\nFizz\nBuzz\nFizz\nFizzBuzz\nFizz\nBuzz\nFizz\nFizz\nBuzz\nFizz\nFizzBuzz\nFizz\nBuzz\nFizz\nFizz\nBuzz")

if __name__ == "__main__":
    unittest.main()
