__author__ = "Shiven"

import unittest
from io import StringIO
from unittest.mock import patch
from maximum import getmaxvalue

class TestMaximum(unittest.TestCase):

    simple_input_1 = iter(["100 123 145 4 90 89 78 87 65 90 1000 189 198 178 167 456 678 890 -1"]).__next__

    @patch("builtins.input", simple_input_1)
    def test_minimum_1(self):
        out = StringIO()
        with patch("sys.stdout", out) as output:
            getmaxvalue()
        output = output.getvalue().strip()
        self.assertEqual(output, "1000")

    simple_input_2 = iter(["6800 9000 -9000 567 890 90 10 11"]).__next__

    @patch("builtins.input", simple_input_2)
    def test_minimum_2(self):
        out = StringIO()
        with patch("sys.stdout", out) as output:
            getmaxvalue()
        output = output.getvalue().strip()
        self.assertEqual(output, "9000")

if __name__ == "__main__":
    unittest.main()
