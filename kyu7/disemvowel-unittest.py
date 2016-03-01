__author__ = "Shiven"
import unittest
import disemvowel

class TestVowel(unittest.TestCase):

	def test_vowel_remove_1(self):
		self.assertEquals(disemvowel.remove_vowels("I am going to America"), " m gng t mrc")

	def test_vowel_remove_2(self):
		self.assertEquals(disemvowel.remove_vowels("aeiou"), "")

	def test_vowel_remove_3(self):
		self.assertEquals(disemvowel.remove_vowels("AEIOUaeiou"), "")

if __name__ == "__main__":
	unittest.main()