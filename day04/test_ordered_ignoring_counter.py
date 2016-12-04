from day04 import OrderedIgnoringCounter


def test_ignoring():
    counter = OrderedIgnoringCounter('aaaaa-bbb-z-y-x', ignore='-')
    assert not ('-', 4) in counter.most_common()


def test_ordered():
    counter = OrderedIgnoringCounter('aaaaa-bbb-z-y-x', ignore='-')
    assert counter.most_common() == [('a', 5), ('b', 3), ('x', 1), ('y', 1), ('z', 1)]
