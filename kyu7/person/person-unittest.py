__author__ ="Shiven"

import unittest
from unittest.mock import patch
import person


class TestPerson(unittest.TestCase):

    @patch("builtins.input", lambda:"")
    def test_person_amIOld(self):
        print("No test implemented")

    @patch("builtins.input", lambda:"")
    def test_person_yearPasses(self):
        print("No test implemented")


if __name__ == "__main__":
    unittest.main()
