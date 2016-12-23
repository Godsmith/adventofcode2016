from day20.range import Range

class Blacklist:
    def __init__(self, list_):
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
