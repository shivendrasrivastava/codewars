__author__ = "Shiven"

import unittest
from io import StringIO
from unittest.mock import patch
from string_reverse import reverse_str

class TestStringReverse(unittest.TestCase):

    simple_input_1 = iter(["Shivendra"]).__next__

    @patch("builtins.input", simple_input_1)
    def test_string_reverse_1(self):
        out = StringIO()
        with patch("sys.stdout", out) as fakeOutput:
            reverse_str()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "ardnevihS")

    simple_input_2 = iter(["I love my honey bunny Shonu cutie pie"]).__next__

    @patch("builtins.input", simple_input_2)
    def test_string_reverse_2(self):
        out = StringIO()
        with patch("sys.stdout", out) as output:
            reverse_str()
        output = output.getvalue().strip()
        self.assertEqual(output, "eip eituc unohS ynnub yenoh ym evol I")

if __name__ == "__main__":
    unittest.main()
