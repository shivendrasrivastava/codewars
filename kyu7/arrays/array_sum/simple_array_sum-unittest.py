__author__ = "Shiven"

import unittest
from unittest.mock import patch
from simple_array_sum import main

class TestSimpleArraySum(unittest.TestCase):

    @patch("builtins.input", lambda: "1 2 3 4 5 6 7")
    def simple_array_sum_1(self):
        self.assertEquals(main(), 28)

    @patch("builtins.input", lambda: "8 9 10 11 12 13")
    def simple_array_sum_2(self):
        self.assertEquals(main(), 63)

if __name__ == "__main__":
    unittest.main()
