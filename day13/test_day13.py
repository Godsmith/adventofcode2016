from day13.day13 import location


def test_location():
    for x, c in enumerate('.#.####.##'):
        assert location(x, 0, 10) == c
