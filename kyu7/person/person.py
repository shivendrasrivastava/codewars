__author__ = "Shiven"

class Person(self):

    age = 0

    #Constructor
    def __init__(self, initialAge):
        if initialAge > 0:
            age = initialAge
        else:
            print("Age is not valid, setting age to 0.")
            age = 0

    #AmIOld
    def amIOld(self):
        if age <= 13:
            print("You are young")
            return "You are young"
        elif age >= 13 and age <= 18:
            print("You are a teenager")
            return "You are a teenager"
        else:
            print("You are old")

    #YearPasses
    def yearPasses(self):
        age = age + 1


    def main(self):
        t = int(input())
        for t in range(0, t):
            age = int(input())
