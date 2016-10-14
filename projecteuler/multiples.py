'''
if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

__author__ = "Shiven"

def sum_multiples(n):
    total = 0
    for x in range(n):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    print(total)
    return total

def sum_multiples_fast(n):
    return int(divisible(3, n-1) + divisible(5, n-1) - divisible(15, n-1))

def divisible(n, p):
    return n * (p/n) * ((p/n) + 1)/2
