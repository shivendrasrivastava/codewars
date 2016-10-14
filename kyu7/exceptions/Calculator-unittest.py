__author__ = "Shiven"


import unittest
from unittest.mock import patch
from io import StringIO
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    sample_input_1 = iter([3, 4]).__next__

    @patch('builtins.input', sample_input_1)
    def test_calculator_1(self):
        cal = Calculator()
        out = StringIO()
        with patch("sys.stdout", out) as fakeOutput:
            cal.calculate()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "81")

    sample_input_2 = iter([-3, -4]).__next__

    @patch('builtins.input', sample_input_2)
    def test_calculator_2(self):
        cal = Calculator()
        out = StringIO()
        with patch("sys.stdout", out) as fakeOutput:
            cal.calculate()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "n and p should be non-negative")

if __name__ == "__main__":
    unittest.main()
