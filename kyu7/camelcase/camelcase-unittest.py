__author__ = "Shiven"

import sys
import unittest
from io import StringIO
from camelcase import countcase
from unittest.mock import patch

class TestCamelCaseCount(unittest.TestCase):

    sample_input_1 = iter(["saveChangesInTheEditor"]).__next__

    @patch("builtins.input", sample_input_1)
    def test_camel_case_count_1(self):
        out = StringIO()
        with patch('sys.stdout', out) as fakeOutput:
            countcase()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "5")

    sample_input_2 = iter(["thisIsAChevroletCamaroWithAV8Engine"]).__next__

    @patch("builtins.input", sample_input_2)
    def test_camel_case_count_2(self):
        out = StringIO()
        with patch('sys.stdout', out) as fakeOutput:
            countcase()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "9")

if __name__ == "__main__":
    unittest.main()
