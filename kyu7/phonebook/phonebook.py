__author__ = "Shiven"

import sys

def contacts():
    n = int(input().strip())
    phone_book = {}
    entries = ()
    for x in range(n):
        entries = input().strip().split(' ')
        phone_book[entries[0]] = entries[1]
    while True:
        query = input().strip()
        if query == "":
            break
        if query in phone_book:
            print(query,"=",phone_book[query], sep='')
        else:
            print("Not found")

if __name__ == "__main__":
    contacts()
