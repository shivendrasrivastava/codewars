__author__ = "Shiven"

import sys
from io import StringIO
import unittest
from unittest.mock import patch
from sock_merchant import sell

class TestSockMerchant(unittest.TestCase):

    sample_input_1 = iter(['9', '10 20 20 10 10 30 50 10 20']).__next__

    @patch("builtins.input", sample_input_1)
    def test_sock_merchant_1(self):
        out = StringIO()
        with patch('sys.stdout', out) as fakeOutput:
            sell()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "3")

    sample_input_2 = iter(['10', '9 9 9 9 9 9 9 9 9 9']).__next__

    @patch("builtins.input", sample_input_2)
    def test_sock_merchant_2(self):
        out = StringIO()
        with patch('sys.stdout', out) as fakeOutput:
            sell()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "5")

    sample_input_3 = iter(['20', '10 10 11 11 12 12 13 13 14 14 15 16 17 18 19 20 20 21 21 22']).__next__

    @patch("builtins.input", sample_input_3)
    def test_sock_merchant_3(self):
        out = StringIO()
        with patch('sys.stdout', out) as fakeOutput:
            sell()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "7")

    sample_input_4 = iter(['1', '100']).__next__

    @patch("builtins.input", sample_input_4)
    def test_sock_merchant_4(self):
        out = StringIO()
        with patch('sys.stdout', out) as fakeOutput:
            sell()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "0")

    sample_input_5 = iter(['2', '1 2']).__next__

    @patch("builtins.input", sample_input_5)
    def test_sock_merchant_5(self):
        out = StringIO()
        with patch('sys.stdout', out) as fakeOutput:
            sell()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "0")

if __name__ == "__main__":
    unittest.main()
