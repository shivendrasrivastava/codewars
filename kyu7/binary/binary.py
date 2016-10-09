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
