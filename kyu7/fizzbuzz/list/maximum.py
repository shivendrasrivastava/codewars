__author__ = "Shiven"

def getmaxvalue():
    int_lst = sorted(list(map(int, input().split())))
    print(int_lst[::-1][0])
