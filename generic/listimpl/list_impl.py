"""
Trying to implement list in python
"""
__author__ = "Shiven"

from array import array

class List():
    """
    This is a list implementation
    """
    arr = None

    def __init__(self):
        """
        Initialize the list with a size
        """
        self.arr = array("i")

    def add(self, value):
        """
        Used to add elements to the list
        """
        self.arr.append(value)

    def remove(self, value):
        """
        Used to remove elements from the list
        """
        self.arr.remove(value)

    def size(self):
        """
        Gets the size of the list
        """
        return len(self.arr)
