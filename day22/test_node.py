from day22.node import Node


def test_viable_pair():
    assert Node.viable_pair(Node(x=0, y=0, used=1, avail=3), Node(x=0, y=1, used=2, avail=1))
    assert not Node.viable_pair(Node(x=0, y=0, used=2, avail=3), Node(x=0, y=1, used=2, avail=1))
    assert not Node.viable_pair(Node(x=0, y=0, used=0, avail=3), Node(x=0, y=1, used=2, avail=1))

    n = Node(x=0, y=0, used=2, avail=3)
    assert not Node.viable_pair(n, n)


def test_from_string():
    assert Node.from_string('/dev/grid/node-x0-y0      93T   71T    22T    76%') == Node(x=0, y=0, used=71, avail=22)


def test_move_data_to():
    node1 = Node(x=0, y=0, used=50, avail=50)
    node2 = Node(x=0, y=1, used=0, avail=100)
    node1.has_target_data = True

    node1.move_data_to(node2)

    assert node1.used == 0
    assert node1.avail == 100
    assert node2.used == 50
    assert node2.avail == 50
    assert not node1.has_target_data
    assert node2.has_target_data
