from day20.blacklist import Blacklist

with open('input.txt') as f:
    b = Blacklist([line for line in f.readlines() if len(line) > 0])
    print(b.lowest_valid_ip)
    print(b.count_allowed_ips())
