__author__ = "Shiven"

import unittest
from unittest.mock import patch
from stringoddeven import main

class TestStringOddEven(unittest.TestCase):

    @patch("builtins.input", lambda: "Shivendra")
    def test_string_oddeven_1(self):
        self.assertEquals(main(), "Sieda hvnr")

    @patch("builtins.input", lambda: "Sonam")
    def test_string_oddeven_2(self):
        self.assertEquals(main(), "Snm oa")


if __name__ == "__main__":
    unittest.main()
