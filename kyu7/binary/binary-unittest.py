__author__ = "Shiven"

import sys, unittest
from unittest.mock import patch
from io import StringIO
from binary import base2

class TestBinary(unittest.TestCase):

    def test_binary_1(self):
        self.assertEqual(base2(5), 1)

    def test_binary_2(self):
        self.assertEqual(base2(13), 2)

    def test_binary_3(self):
        self.assertEqual(base2(439), 3)

if __name__ == "__main__":
    unittest.main()
