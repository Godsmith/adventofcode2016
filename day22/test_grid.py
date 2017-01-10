import pytest

from day22.grid import Grid
from day22.node import Node


@pytest.fixture()
def grid2x2():
    nodes = map(Node.from_string, ['/dev/grid/node-x0-y0      93T   71T    22T    76%',
                                   '/dev/grid/node-x1-y0      93T   71T    22T    76%',
                                   '/dev/grid/node-x0-y1      93T   71T    22T    76%',
                                   '/dev/grid/node-x1-y1      93T   71T    22T    76%'])
    return Grid(nodes)


def test_adjacent_nodes(grid2x2):
    assert len(grid2x2._adjacent_nodes(grid2x2.get_node(0, 0))) == 2
