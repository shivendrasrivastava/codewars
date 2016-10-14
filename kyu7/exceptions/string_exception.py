__author__ = "Shiven"

def convert():
    try:
        int_s = int(input().strip())
        print(int_s)
    except ValueError:
        print("Bad String")
