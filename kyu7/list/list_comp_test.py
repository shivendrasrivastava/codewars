__author__ = "Shiven"

import unittest
from unittest.mock import patch
from list_comp import comprehend

class TestListComp(unittest.TestCase):

    @patch('builtins.input', lambda:"1")
    def test_list_comp_1(self):
        self.assertEquals(comprehend(), 2)

if __name__ == "__main__":
    unittest.main()
