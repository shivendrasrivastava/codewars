__author__ = "Shiven"

def main():
    summation = 0
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    for x in range(len(arr)):
        summation = summation + arr[x]
    return summation
