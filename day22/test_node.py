from day22.node import Node


def test_viable_pair():
    assert Node.viable_pair(Node(used=1, avail=3), Node(used=2, avail=1))
    assert not Node.viable_pair(Node(used=2, avail=3), Node(used=2, avail=1))
    assert not Node.viable_pair(Node(used=0, avail=3), Node(used=2, avail=1))

    n = Node(used=2, avail=3)
    assert not Node.viable_pair(n, n)


def test_from_string():
    assert Node.from_string('/dev/grid/node-x0-y0      93T   71T    22T    76%') == Node(name='/dev/grid/node-x0-y0',
                                                                                         used=71, avail=22)
