__author__ = "Shiven"

import unittest
import powers

class TestPowers(unittest.TestCase):

	def test_powers_1(self):
		self.assertEquals(powers.powers([1,2,3,4,5,6,7,8,9,10]), 1024)

	def test_powers_2(self):
		self.assertEquals(powers.powers([1,2,]), 4)

	def test_powers_3(self):
		self.assertEquals(powers.powers([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]), 1073741824)

if __name__ == '__main__':
	unittest.main()