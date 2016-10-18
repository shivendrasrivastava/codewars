__author__ = "Shiven"

import unittest
from io import StringIO
from unittest.mock import patch
from calculate_multiples import calculate


class TestCalculateMultiples(unittest.TestCase):

    simple_input_1 = iter(["3 5"]).__next__

    @patch("builtins.input", simple_input_1)
    def test_calculate_multiples_1(self):
        out = StringIO()
        with patch("sys.stdout", out) as output:
            calculate()
        output = output.getvalue().strip()

if __name__ == "__main__":
    unittest.main()
