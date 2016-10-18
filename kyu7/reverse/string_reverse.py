__author__ = "Shiven"

def reverse_str():
    str_to_reverse = input().strip()
    str_list = list(str_to_reverse)
    reversed_str = "".join(str_list[::-1])
    print(reversed_str)
    return reversed_str
