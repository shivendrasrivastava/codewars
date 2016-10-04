__author__ = "Shiven"

import unittest
from ..kyu7.oddeven import oddeven

class TestOddEven(unittest.TestCase):

    def test_odd_even_1(self):
        self.assertEquals(oddeven(3), "Weird")

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    unittest.main()
