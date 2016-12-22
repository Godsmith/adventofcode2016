from day21.scrambler import Scrambler


def test_rotate_right():
    assert Scrambler.do('rotate right 3 steps', 'abcde') == 'cdeab'


def test_rotate_left():
    assert Scrambler.do('rotate left 3 steps', 'abcde') == 'deabc'


def test_rotate_based_on_position():
    assert Scrambler.do('rotate based on position of letter a', 'abcde') == 'eabcd'
    assert Scrambler.do('rotate based on position of letter b', 'abcde') == 'deabc'
    assert Scrambler.do('rotate based on position of letter e', 'abcde') == 'eabcd'


def test_swap_position():
    assert Scrambler.do('swap position 2 with position 0', 'abcde') == 'cbade'


def test_swap_letter():
    assert Scrambler.do('swap letter c with letter d', 'abcde') == 'abdce'


def test_reverse():
    assert Scrambler.do('reverse positions 1 through 3', 'abcde') == 'adcbe'


def test_move():
    assert Scrambler.do('move position 2 to position 4', 'abcde') == 'abdec'
    assert Scrambler.do('move position 4 to position 2', 'abcde') == 'abecd'


def test_do_all():
    operations = ['swap position 4 with position 0', 'swap letter d with letter b', 'reverse positions 0 through 4',
                  'rotate left 1 step', 'move position 1 to position 4', 'move position 3 to position 0',
                  'rotate based on pposition of letter b', 'rotate based on position of letter d']
    assert Scrambler.do_all(operations, 'abcde') == 'decab'

