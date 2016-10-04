__author__="Shiven"

import unittest
from unittest.mock import patch
from evenodd import main

class TestEvenOdd(unittest.TestCase):

    @patch("builtins.input", lambda: "3")
    def test_even_odd_1(self):
        self.assertEquals(main(), "Weird")

    @patch("builtins.input", lambda: "4")
    def test_even_odd_2(self):
        self.assertEquals(main(), "Not Weird")

    @patch("builtins.input", lambda: "8")
    def test_even_odd_3(self):
        self.assertEquals(main(), "Weird")

    @patch("builtins.input", lambda: "22")
    def test_even_odd_4(self):
        self.assertEquals(main(), "Not Weird")

    @patch("builtins.input", lambda: "23")
    def test_even_odd_5(self):
        self.assertEquals(main(), "Weird")

if __name__ == "__main__":
    unittest.main()
