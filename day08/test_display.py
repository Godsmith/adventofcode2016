from unittest.mock import patch

from day08.display import Display


def test_str():
    display = Display(rows=2, columns=3)
    assert str(display) == '...\n...'


def test_rect():
    display = Display(rows=3, columns=7)
    display.rect(width=3, height=2)
    assert str(display) == '###....\n###....\n.......'


def test_get_column():
    display = Display(rows=3, columns=7)
    display.rect(width=3, height=2)
    assert display._get_column(1) == ['#', '#', '.']


def test_get_row():
    display = Display(rows=3, columns=7)
    display.rect(width=3, height=2)
    assert display._get_row(0) == ['#', '#', '#', '.', '.', '.', '.']


def test_rotate_array():
    assert Display._rotate_array([1, 2, 3, 4], 1) == [4, 1, 2, 3]
    assert Display._rotate_array([1, 2, 3, 4], 4) == [1, 2, 3, 4]
    assert Display._rotate_array([1, 2, 3, 4], 8) == [1, 2, 3, 4]


def test_rotate_column():
    display = Display(rows=3, columns=7)
    display.rect(width=3, height=2)
    display.rotate_column(x=1, steps=1)
    assert str(display) == '#.#....\n###....\n.#.....'


def test_rotate_row():
    display = Display(rows=3, columns=7)
    display.rect(width=3, height=2)
    display.rotate_column(x=1, steps=1)
    display.rotate_row(y=0, steps=4)
    assert str(display) == '....#.#\n###....\n.#.....'


def test_lit_pixels():
    display = Display(rows=3, columns=7)
    display.rect(width=3, height=2)
    assert display.lit_pixels() == 6


def test_command_rect():
    with patch.object(Display, 'rect') as mock_method:
        display = Display(rows=3, columns=7)
        display.command('rect 1x2')
        mock_method.assert_called_once_with(1, 2)


def test_command_rotate_row():
    with patch.object(Display, 'rotate_row') as mock_method:
        display = Display(rows=3, columns=7)
        display.command('rotate row y=1 by 20')
        mock_method.assert_called_once_with(1, 20)


def test_command_rotate_column():
    with patch.object(Display, 'rotate_column') as mock_method:
        display = Display(rows=3, columns=7)
        display.command('rotate column x=19 by 2')
        mock_method.assert_called_once_with(19, 2)
