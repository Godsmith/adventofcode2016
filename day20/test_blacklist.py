from day20.blacklist import Blacklist


class TestLowestValidIp:
    def test_new_range_adjacent_to_two_ranges(self):
        b = Blacklist(['0-13', '18-23', '14-17'])
        assert b.lowest_valid_ip == 24

    # def test_real_example(self):
    #     b = Blacklist(['0-296167', '296168-338264', '356899-526908', '318586-356898', ])
    #     assert b.lowest_valid_ip == 526909

    def test_example(self):
        b = Blacklist(['5-8', '0-2', '4-7'])
        assert b.lowest_valid_ip == 3

    def test_neighboring_ranges(self):
        b = Blacklist(['0-13', '14-17', '19-23'])
        assert b.lowest_valid_ip == 18
