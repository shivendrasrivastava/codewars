__author__ = "Shiven"
import re

def calculate_sum():
    handle = open("sample-text.txt")
    complete_list = []
    for line in handle:
        number_list = re.findall('[0-9]\S+',line.strip())
        if number_list is not None:
            for number in number_list:
                complete_list.append(int(number))
    print sum(complete_list)

if __name__ == "__main__":
    calculate_sum()
