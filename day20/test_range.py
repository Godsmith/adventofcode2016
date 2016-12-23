from day20.range import Range


def test_can_be_combined():
    assert Range(1, 2).can_be_combined(Range(3, 4))
    assert Range(1, 3).can_be_combined(Range(3, 4))
    assert Range(1, 4).can_be_combined(Range(3, 5))
    assert Range(1, 4).can_be_combined(Range(2, 3))
    assert Range(3, 5).can_be_combined(Range(1, 2))
    assert not Range(3, 5).can_be_combined(Range(0, 1))
    assert not Range(0, 2).can_be_combined(Range(4, 5))


def test_combine():
    assert Range.combine([Range(1, 2)]) == Range(1, 2)
    assert Range.combine([Range(1, 2), Range(3, 4)]) == Range(1, 4)
    assert Range.combine([Range(4, 6), Range(1, 2), Range(3, 5)]) == Range(1, 6)
