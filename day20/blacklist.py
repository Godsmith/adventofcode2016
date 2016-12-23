from day20.range import Range


class Blacklist:
    def __init__(self, list_, highest_ip=2 ** 32 - 1):
        self.highest_ip = highest_ip
        self.ranges = set()
        for s in list_:
            low, high = tuple(map(int, s.split('-')))
            new_range = Range(low, high)
            ranges_that_can_be_combined = []
            for range_ in self.ranges:
                if new_range.can_be_combined(range_):
                    ranges_that_can_be_combined.append(range_)

            for range_ in ranges_that_can_be_combined:
                self.ranges.remove(range_)
            combined_range = Range.combine(ranges_that_can_be_combined + [new_range])
            self.ranges.add(combined_range)

    @property
    def lowest_valid_ip(self):
        return [r.high + 1 for r in self.ranges if r.low == 0][0]

    def count_allowed_ips(self):
        sorted_ranges = sorted(self.ranges, key=lambda x: x.low)
        ips = self.highest_ip - sorted_ranges[-1].high
        for i, _ in enumerate(sorted_ranges[:-1]):
            ips += sorted_ranges[i + 1].low - sorted_ranges[i].high - 1
        return ips
