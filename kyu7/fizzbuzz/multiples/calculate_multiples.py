__author__ = "Shiven"

def calculate():
    for x in range(101):
        if x % 3 == 0 and x % 5 == 0:
            print(x,"FizzBuzz")
        if x % 3 == 0 and x % 5 != 0:
            print(x,"Fizz")
        if x % 5 == 0 and x % 3 != 0:
            print(x,"Buzz")

if __name__ == "__main__":
    calculate()
