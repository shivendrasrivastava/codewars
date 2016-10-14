__author__ = "Shiven"

class Calculator(object):

    def __init__(self):pass

    def calculate(self):
        n = int(input())
        p = int(input())
        if n < 0 or p < 0:
            print("n and p should be non-negative")
        else:
            print(n**p)
