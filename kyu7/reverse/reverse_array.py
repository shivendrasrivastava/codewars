__author__ = "Shiven"

def main():
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    print(*reversed(arr), sep=" ")
    #print("6 5 4 3 2 1")
