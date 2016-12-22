class Range:
    def __init__(self, low, high):
        self.low = low
        self.high = high


class Blacklist:
    def __init__(self, list_):
        self.ranges = []
        for s in list_:
            low, high = tuple(s.split('-'))
            for range_ in self.ranges:
                if range_.low > high:
                    continue
                if range_.high < low:
                    continue
                if low < range_.low:
                    range_.low = low
                if high > range_.high:
                    range_.high = high
                break
            else:
                self.ranges.append(Range(low, high))

    @property
    def lowest_valid_ip(self):
        return [r.high + 1 for r in self.ranges if r.low == 0][0]
