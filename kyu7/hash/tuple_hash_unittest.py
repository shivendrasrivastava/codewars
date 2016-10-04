__author__ = "Shiven"

import unittest
from unittest.mock import patch
import tuple_hash
import UserInput

class TestHash(unittest.TestCase):

    @patch("UserInput.read_integer_input")
    @patch("UserInput.read_integer_tuple_input")
    def test_hash_1(self, mock_integer_input, mock_integer_tuple_input):
        tuple_hash = hash(mock_integer_tuple_input)
        self.assertEquals(tuple_hash, tuple_hash.gen_hash())

if __name__ == "__main__":
    unittest.main()
