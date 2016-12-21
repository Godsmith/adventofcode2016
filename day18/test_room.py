from day18.room import Room


def test_make_tile():
    assert Room.make_tile('^^.') == '^'
    assert Room.make_tile('.^^') == '^'
    assert Room.make_tile('^..') == '^'
    assert Room.make_tile('..^') == '^'

    assert Room.make_tile('...') == '.'
    assert Room.make_tile('.^.') == '.'
    assert Room.make_tile('^^^') == '.'
    assert Room.make_tile('^.^') == '.'


def test_make_row():
    assert Room.make_row('..^^.') == '.^^^^'
    assert Room.make_row('.^^^^') == '^^..^'


def test_make_rows():
    assert Room.make_rows('..^^.', 3) == ['..^^.', '.^^^^', '^^..^']


def test_count_safe_tiles():
    assert Room.count_safe_tiles(Room.make_rows('..^^.', 3)) == 6
