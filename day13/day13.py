def location(x, y, favorite_number):
    value = x * x + 3 * x + 2 * x * y + y + y * y + favorite_number
    binary = bin(value)[2:]
    if binary.count('1') % 2 == 0:
        return '.'
    else:
        return '#'
