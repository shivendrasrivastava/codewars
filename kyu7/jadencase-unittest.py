import unittest
import jadencase

class TestJadenCaseStrings(unittest.TestCase):

	def test_jaden_case(self):
		self.assertEquals(jadencase.toJadenCase("hi i am shivendra"), "Hi I Am Shivendra")

	def test_jaden_case_1(self):
		self.assertEquals(jadencase.toJadenCase("where are@##%(*$&*#"), "Where Are@##%(*$&*#")

if __name__ == '__main__':
	unittest.main()
