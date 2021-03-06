def int_list_from_string(s):
    s = s.strip()  # To remove line breaks etc
    list_with_some_empty_strings = s.split(' ')
    list_without_empty_strings = [i for i in list_with_some_empty_strings if i != '']
    return list(map(int, list_without_empty_strings))


def is_triangle(int_list):
    sorted_list = sorted(int_list)
    return sum(sorted_list[0:2]) > sorted_list[2]


def chunk(list_, n):
    for i in range(0, len(list_), n):
        yield list_[i:i + n]


def transpose(l):
    return list(map(list, zip(*l)))


def column_lists_from_row_lists(list_of_lists):
    for partial_list in chunk(list_of_lists, len(list_of_lists[0])):
        for row in transpose(partial_list):
            yield row


def count_triangles(int_lists):
    return [is_triangle(l) for l in int_lists].count(True)


def count_column_triangles(string_list):
    int_lists = [int_list_from_string(s) for s in string_list]
    new_int_lists = column_lists_from_row_lists(int_lists)
    return count_triangles(new_int_lists)


def test_chunk():
    list_ = [1, 2, 3, 4, 5, 6]
    assert list(chunk(list_, 3)) == [[1, 2, 3], [4, 5, 6]]


def test_int_list_from_string():
    assert int_list_from_string('11 22 33') == [11, 22, 33]
    assert int_list_from_string('  11  22       33\n') == [11, 22, 33]


def test_is_triangle():
    assert is_triangle([3, 3, 3]) is True
    assert is_triangle([1, 1, 8]) is False


def test_transpose():
    assert transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


def test_column_lists_from_row_lists():
    assert list(column_lists_from_row_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]])) == [
        [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9]]


def test_column_triangles():
    input_ = ["101 301 501",
              "102 302 502",
              "103 303 503",
              "201 401 601",
              "202 402 602",
              "203 403 603"]
    assert count_column_triangles(input_) == 6


with open('input.txt') as f:
    lines = f.readlines()
    print(count_triangles([int_list_from_string(s) for s in lines]))
    print(count_column_triangles(lines))
