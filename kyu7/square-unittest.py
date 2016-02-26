__author__ = "Shiven"

import unittest
import is_square

class TestPowers(unittest.TestCase):

	def test_square_1(self):
		self.assertEquals(is_square.check_square(3), False)

	def test_square_2(self):
		self.assertEquals(is_square.check_square(25), True)

	def test_square_3(self):
		self.assertEquals(is_square.check_square(676), True)

if __name__ == '__main__':
	unittest.main()