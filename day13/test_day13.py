from day13.location import location


def test_location():
    for x, c in enumerate('.#.####.##'):
        assert location(x, 0, 10) == c
