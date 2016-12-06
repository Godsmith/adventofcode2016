from collections import Counter


def most_frequent_for_each_position(lines):
    out = ''
    for i in range(len(lines[0])):
        counter = Counter([line[i] for line in lines])
        out += counter.most_common(1)[0][0]
    return out


def least_frequent_for_each_position(lines):
    out = ''
    for i in range(len(lines[0])):
        counter = Counter([line[i] for line in lines])
        out += counter.most_common(26)[-1][0]
    return out
