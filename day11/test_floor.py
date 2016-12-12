from day11.floor import Floor


def test_legal():
    floor = Floor({'HG', 'HM'})
    assert floor.is_legal()

    floor = Floor({})
    assert floor.is_legal()

    floor = Floor({'HG', 'PG'})
    assert floor.is_legal()

    floor = Floor({'HG', 'PM'})
    assert not floor.is_legal()


def test_eq():
    assert Floor({'HG', 'HM'}) == Floor({'HG', 'HM'})
    assert not Floor({'HM'}) == Floor({'HG', 'HM'})
    assert not Floor({'HM'}) == 'sdf'


def test_without():
    floor = Floor({'HG', 'HM'})
    assert floor.without({'HG'}) == Floor({'HG', 'HM'})
