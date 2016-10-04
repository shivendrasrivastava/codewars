__author__ = "Shiven"

class UserInput():

    def read_integer_input(self):
        return int(input().strip())

    def read_integer_tuple_input(self):
        return tuple(int(x.strip()) for x in input().split(' '))
