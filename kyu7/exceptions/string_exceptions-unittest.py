__author__ = "Shiven"

import unittest
from string_exception import convert
from unittest.mock import patch
from io import StringIO

class TestStringException(unittest.TestCase):

    sample_input_1 = iter(['32']).__next__

    @patch("builtins.input", sample_input_1)
    def test_convert_1(self):
        out = StringIO()
        with patch('sys.stdout', out) as fakeOutput:
            convert()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "32")

    sample_input_2 = iter(["Shivendra"]).__next__

    @patch("builtins.input", sample_input_2)
    def test_convert_2(self):
        out = StringIO()
        with patch('sys.stdout', out) as fakeOutput:
            convert()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "Bad String")

if __name__ == "__main__":
    unittest.main()
