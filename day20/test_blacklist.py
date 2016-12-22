from day20.blacklist import Blacklist

def test_lowest_valid_ip():
    b = Blacklist(['5-8', '0-2', '4-7'])
    assert b.lowest_valid_ip == 3

