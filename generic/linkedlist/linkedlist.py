"""
Linked list implementation in python
"""
__author__ = "Shiven"

class LinkedList():
    """
    Linked list class
    """
    counter = 0
    head = None

    def __init__(self):
        """
        Constructor for linkedlist
        """

    def increment(self):
        """
        Increments the counter
        """
        self.counter += 1

    def decrement(self):
        """
        Decrements the counter
        """
        self.counter -= 1


    def add(self, data):
        """
        Adds value to linkedlist
        """
        if self.head is None:
            self.head = Node(data)

        temp_node = Node(data)
        current = self.head

        if not current is None:
            while not current.get_next() is None:
                current = current.get_next()

            #Setting the element in the end
            current.set_next(temp_node)
            self.increment()

    def get_count(self):
        """
        Returns the counter value
        """
        return self.counter

    def get(self, index):
        """
        Gets the value at the specified index
        """
        if index < 0:
            return None

        current = None
        if not self.head is None:
            current = self.head.get_next()
            for _val in range(0, index):
                if current.get_next() is None:
                    return None

                current = current.get_next()
            return current.get_data()
        return None

    def remove(self, index):
        """
        Removes the value at the specified index
        """
        if (index < 1) or (index > self.size()):
            return None

        current = self.head
        if not self.head is None:
            for _val in range(0, index):
                if current.get_next() is None:
                    return None

                current = current.get_next()
            current.set_next(current.get_next().get_next())
            self.decrement()
            return True

        return False




    def size(self):
        """
        Returns the size of the linkedlist
        """
        return self.get_count()

class Node():
    """
    Node class to hold the data for the linkedlist
    """
    nxt = None
    data = None

    def __init__(self, value):
        """
        Constructor that initializes a node
        """
        self.nxt = None
        self.data = value

    def get_data(self):
        """
        Returns the data
        """
        return self.data

    def set_data(self, value):
        """
        Sets the data
        """
        self.data = value

    def get_next(self):
        """
        Returns the next value
        """
        return self.nxt

    def set_next(self, nxt_value):
        """
        Sets the next value
        """
        self.nxt = nxt_value
