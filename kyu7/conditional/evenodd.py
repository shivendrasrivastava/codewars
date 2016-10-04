__author__ ="Shiven"

def main():
    result = "Weird"
    number = int(input().strip())
    if number % 3 == 0:
        result = "Weird"
    if number % 2 == 0:
        if (number >=2 and number <=5) or (number > 20):
            result = "Not Weird"
        if number >= 6 and number <= 20:
            result = "Weird"
    print(result)
    return result
