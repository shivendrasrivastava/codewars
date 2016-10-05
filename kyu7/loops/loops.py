__author__ = "Shiven"

def main():
    value = get_input()
    return value

def get_input():
    value = input()
    if type(value) != int:
        value = int(value.strip())
    run_loop(value)
    return value

def run_loop(value):
    for x in range(1, 11):
        result = value * x
        print(value, 'x' ,x, ' = ',result)
