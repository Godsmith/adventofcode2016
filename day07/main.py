from day07.ipv7_string import Ipv7String

with open('input.txt') as f:
    lines = f.readlines()
    print([Ipv7String(line).supports_tls() for line in lines].count(True))
    print([Ipv7String(line).supports_ssl() for line in lines].count(True))
