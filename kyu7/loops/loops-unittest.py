__author__ = "Shiven"

import unittest
from unittest.mock import patch
from loops import main

class TestLoops(unittest.TestCase):

    @patch("builtins.input", lambda: 2)
    def test_loops_input_1(self):
        self.assertEquals(main(), 2)

    @patch("builtins.input", lambda: "4")
    def test_loops_input_2(self):
        self.assertEquals(main(), 4)

if __name__ == "__main__":
    unittest.main()
