__author__ = "Shiven"

def calculate():
    number = int(input().strip())
    fizz = int(input().strip())
    buzz = int(input().strip())
    output = ""
    for x in range(1,number+1):
        if x % fizz == 0:
            output += "Fizz"
        if x % buzz == 0:
            output += "Buzz"
        if output:
            print(output)
        output = ""

if __name__ == "__main__":
    calculate()
