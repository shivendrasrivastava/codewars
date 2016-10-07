__author__ = "Shiven"

def sell():
    n = int(input().strip())
    socks = [int(s_temp) for s_temp in input().strip().split(' ')]
    socks = sorted(socks)
    pairs = 0
    sock_dict = dict()
    sock_len = len(socks)-1
    if sock_len != 0:
        for x in range(sock_len):
            if socks[x] not in sock_dict:
                pairs = 1
            if socks[x] == socks[x+1]:
                pairs += 1
                sock_dict[socks[x]] = pairs
        #print(sock_dict)
        total_pair = 0
        for key, value in sock_dict.items():
            total_pair += int(value/2)
    else:
        total_pair = 0
    print(total_pair)


if __name__ == "__main__":
    sell()
