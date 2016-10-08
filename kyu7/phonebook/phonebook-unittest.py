__author__ = "Shiven"

import unittest
from io import StringIO
from phonebook import contacts
from unittest.mock import patch

class TestPhoneBook(unittest.TestCase):

    sample_input_1 = iter(['3', 'sam 99912222', 'tom 11122222','harry 12299933', 'sam', 'edward', 'harry', '']).__next__

    @patch("builtins.input", sample_input_1)
    def test_phone_book_1(self):
        out = StringIO()
        with patch('sys.stdout', out) as fakeOutput:
            contacts()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "sam=99912222\nNot found\nharry=12299933")

if __name__ == "__main__":
    unittest.main()
