__author__="Shiven"

import sys

def oddeven():
    number = int(input().strip())
    if 2<=number<=5 and number % 2 == 0:
        print("Not Weird")
    if 6<=number<=20 and number % 2 == 0:
        print("Weird")
    if number > 20 and number % 2 == 0:
        print("Not Weird")
    if number % 3 == 0:
        print("Weird")
