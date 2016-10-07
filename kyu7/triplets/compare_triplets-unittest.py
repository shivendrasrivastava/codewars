__author__ = "Shiven"

import sys
from io import StringIO
import unittest
from unittest.mock import patch
from compare_triplets import compare

class TestCompareTriplets(unittest.TestCase):

    fake_input = iter(['1 2 3', '4 5 6']).__next__

    @patch("builtins.input", fake_input)
    def test_compare_triplets_1(self):
        out = StringIO()
        with patch('sys.stdout', new = StringIO()) as fakeOutput:
            compare()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "0 3")


if __name__ == "__main__":
    unittest.main()
