from day11.floor import Floor


def test_legal():
    floor = Floor('F1', {'HG', 'HM'})
    assert floor.is_legal()

    floor = Floor('F1')
    assert floor.is_legal()

    floor = Floor('F1', {'HG', 'PG'})
    assert floor.is_legal()

    floor = Floor('F1', {'HG', 'LG', 'PG'})
    assert floor.is_legal()

    floor = Floor('F1', {'HG', 'PM'})
    assert not floor.is_legal()

    floor = Floor('F1', {'HM', 'PM', 'CM'})
    assert not floor.is_legal()


def test_eq():
    assert Floor('F1', {'HG', 'HM'}) == Floor('F1', {'HG', 'HM'})
    assert not Floor('F1', {'HM'}) == Floor('F1', {'HG', 'HM'})
    assert not Floor('F1', {'HM'}) == 'sdf'


def test_without():
    floor = Floor('F1', {'HG', 'HM'})
    assert floor.without({'HG'}) == Floor('F1', {'HM'})


def test_translated():
    floor = Floor('F1', {'E', 'HG', 'HM', 'LM'})
    assert floor.translated({'H': 'L', 'L': 'H'}) == Floor('F1', {'E', 'LG', 'LM', 'HM'})
