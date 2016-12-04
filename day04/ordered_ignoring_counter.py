from collections import Counter


class OrderedIgnoringCounter(Counter):
    def __init__(self, *args, **kwds):
        ignore = None
        if 'ignore' in kwds:
            ignore = kwds['ignore']
            del kwds['ignore']
        super().__init__(*args, **kwds)
        del self[ignore]

    def most_common(self, n=None):
        most_common_super = super().most_common(n)
        counts = [t[1] for t in most_common_super]
        sorted_counts = sorted(set(counts), reverse=True)
        all_tuples = []
        for count in sorted_counts:
            tuples_with_this_count = [t for t in most_common_super if t[1] == count]
            sorted_tuples = sorted(tuples_with_this_count, key=lambda t: t[0])
            all_tuples.extend(sorted_tuples)
        return all_tuples
