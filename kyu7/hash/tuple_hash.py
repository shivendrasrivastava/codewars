__author__ = "Shiven"

def gen_hash():
    #get the tuple size from user
    tuple_size = int(input().strip())
    int_tuple = tuple(int(x.strip()) for x in input().split(' '))
    hash_value = hash(int_tuple)
    print(hash_value)
    return hash_value
