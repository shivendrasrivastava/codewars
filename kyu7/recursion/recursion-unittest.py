__author__ = "Shiven"

import unittest
import sys
from recursion import factorial
from unittest.mock import patch
from io import StringIO

class TestRecursion(unittest.TestCase):

    def test_recursion_1(self):
        self.assertEqual(factorial(3), 6)

    def test_recursion_2(self):
        self.assertEqual(factorial(4), 24)

    def test_recursion_3(self):
        self.assertEqual(factorial(5), 120)

    def test_recursion_4(self):
        self.assertEqual(factorial(120), 6689502913449127057588118054090372586752746333138029810295671352301633557244962989366874165271984981308157637893214090552534408589408121859898481114389650005964960521256960000000000000000000000000000)

if __name__ == "__main__":
    unittest.main()
