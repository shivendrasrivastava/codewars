__author__ = "Shiven"

import unittest
from unittest.mock import patch
from bigsum import main

class TestBigSum(unittest.TestCase):

    @patch("builtins.input", lambda: "1000000012 1000000022 1000000032 1000000042")
    def test_big_sum_1(self):
        self.assertEqual(main(), 4000000108)

    @patch("builtins.input", lambda: "1222005500 1222005600 1222005700 1222005800")
    def test_big_sum_2(self):
        self.assertEqual(main(), 4888022600)

if __name__ == "__main__":
    unittest.main()
