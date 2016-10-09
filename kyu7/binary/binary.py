'''
Objective
Today, we are working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

Explanation

Sample Case 1:
The binary representation of 5 is 101 , so the maximum number of consecutive 1's is 1.

Sample Case 2:
The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.
'''

__author__ = "Shiven"

def base2(n):
    if n == 2:
        return 1
    bin_str = bin(n)[2:]
    bin_list = list(bin_str)
    counter = 0
    count_list = []
    found_zero = False
    for x in range(len(bin_list)):
        if '1' == bin_list[x]:
            counter += 1
            count_list.append(counter)
        else:
            found_zero = True
            counter = 0
    print(count_list)
    return max(count_list)
