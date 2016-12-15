from day13 import location

for y in range(40):
    print(''.join([location(x, y, 1362) for x in range(32)]))
