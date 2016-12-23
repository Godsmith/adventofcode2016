class Range:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __repr__(self):
        return 'Range<%s-%s>' % (self.low, self.high)

    def __hash__(self):
        return hash(tuple([self.low, self.high]))

    def __eq__(self, other):
        return self.low == other.low and self.high == other.high

    @classmethod
    def combine(cls, ranges):
        lowest = min([r.low for r in ranges])
        highest = max([r.high for r in ranges])
        return cls(lowest, highest)

    def can_be_combined(self, range_):
        return not (self.high < range_.low - 1 or self.low > range_.high + 1)
