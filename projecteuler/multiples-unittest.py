__author__ = "Shiven"

import unittest
from unittest.mock import patch
from multiples import sum_multiples, sum_multiples_fast
from io import StringIO
import cProfile
import time

class TestMultiples(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.3f" % (self.id(), t))

    def test_multiples_1(self):
        self.assertEqual(sum_multiples(10), 23)

    def test_multiples_2(self):
        self.assertEqual(sum_multiples(1000), 233168)

    def test_multiple_3(self):
        self.assertEqual(sum_multiples_fast(1000), 233168)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMultiples)
    unittest.TextTestRunner(verbosity=0).run(suite)
