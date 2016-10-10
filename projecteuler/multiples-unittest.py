__author__ = "Shiven"

import unittest
from unittest.mock import patch
from multiples import sum_multiples
from io import StringIO

class TestMultiples(unittest.TestCase):

    def test_multiples_1(self):
        self.assertEqual(sum_multiples(10), 23)

    def test_multiples_2(self):
        self.assertEqual(sum_multiples(1000), 233168)

if __name__ == "__main__":
    unittest.main()
