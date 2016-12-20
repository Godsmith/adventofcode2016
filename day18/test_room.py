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
