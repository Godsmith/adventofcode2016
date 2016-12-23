from day20.blacklist import Blacklist


class TestLowestValidIp:
    def test_new_range_adjacent_to_two_ranges(self):
        b = Blacklist(['0-13', '18-23', '14-17'])
        assert b.lowest_valid_ip == 24

    def test_example(self):
        b = Blacklist(['5-8', '0-2', '4-7'])
        assert b.lowest_valid_ip == 3

    def test_neighboring_ranges(self):
        b = Blacklist(['0-13', '14-17', '19-23'])
        assert b.lowest_valid_ip == 18


class TestCountAllowedIps:
    def test_standard(self):
        b = Blacklist(['0-13', '14-17', '19-23'], highest_ip=23)
        assert b.count_allowed_ips() == 1

        b = Blacklist(['0-13', '14-17', '19-23'], highest_ip=24)
        assert b.count_allowed_ips() == 2

        b = Blacklist(['0-11', '14-17', '19-23'], highest_ip=24)
        assert b.count_allowed_ips() == 4
