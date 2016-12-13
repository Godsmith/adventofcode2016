from day11.move import Move


def test_len():
    move = Move('F1', {'FG', 'FM'})
    assert len(move) == 2
