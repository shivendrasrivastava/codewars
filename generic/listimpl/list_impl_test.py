"""
Test case for list
"""

__author__ = "Shiven"

import unittest
from list_impl import List

class TestList(unittest.TestCase):
    """
    This class is used to test the list implementation
    """

    def test_list_add(self):
        """
        Test add functionality of the list class
        """
        lst = List()
        lst.add(1)
        lst.add(2)
        self.assertEqual(lst.size(), 2)

    def test_list_remove(self):
        """
        Test list remove functionality of the list class
        """
        lst = List()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        lst.remove(2)
        self.assertEqual(lst.size(), 2)

    def test_list_size(self):
        """
        Test the size functionality of the list
        """
        lst = List()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        lst.add(4)
        self.assertEqual(lst.size(), 4)

if __name__ == '__main__':
    unittest.main()
