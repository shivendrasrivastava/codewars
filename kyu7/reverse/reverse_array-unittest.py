__author__ = "Shiven"

import sys
import unittest
from unittest.mock import patch
from reverse_array import main
from io import TextIOWrapper, BytesIO
from contextlib import contextmanager
from io import StringIO

class TestReverseArray(unittest.TestCase):

    @patch("builtins.input", lambda: "1 2 3 4 5 6")
    def test_reverse_array_1(self):
        out = StringIO()
        with patch('sys.stdout', new = StringIO()) as fakeOutput:
            main()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "6 5 4 3 2 1")

    @patch("builtins.input", lambda: "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1")
    def test_reverse_array_2(self):
        out = StringIO()
        with patch('sys.stdout', new = StringIO()) as fakeOutput:
            main()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")

if __name__ == "__main__":
    unittest.main()
