__author__ = "Shiven"


def main():
    sum = 0
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    for x in range(len(arr)):
        sum = sum + arr[x]
    print(sum)
    return sum
