import sys


def int_list_from_string(s):
    s = s.strip()
    list_with_some_empty_strings = s.split(' ')
    list_without_empty_strings = [i for i in list_with_some_empty_strings if i != '']
    return list(map(int, list_without_empty_strings))


def is_triangle(int_list):
    sorted_list = sorted(int_list)
    return sum(sorted_list[0:2]) > sorted_list[2]


def test_int_list_from_string():
    assert int_list_from_string('11 22 33') == [11, 22, 33]
    assert int_list_from_string('  11  22       33\n') == [11, 22, 33]


def test_is_triangle():
    assert is_triangle([3, 3, 3]) == True
    assert is_triangle([1, 1, 8]) == False


def test_column_triangles():
    input_ = ["101 301 501",
              "102 302 502",
              "103 303 503",
              "201 401 601",
              "202 402 602",
              "203 403 603"]


count = 0
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        print('"' + line + '"')
        int_list = int_list_from_string(line)
        if is_triangle(int_list):
            count += 1
print(count)
