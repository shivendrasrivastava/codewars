__author__ = "Shiven"

def main():
    inp_str = input().strip()
    str_length = len(inp_str)
    odd_string = ""
    even_string = ""
    list_array = list(inp_str)
    for x in range(0,len(list_array)):
        if x % 2 == 0:
            even_string = even_string + list_array[x]
        else:
            odd_string = odd_string + list_array[x]
            print(odd_string)
    resultant_string = even_string + " " + odd_string
    return resultant_string
