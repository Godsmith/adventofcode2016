import pytest

from day22.grid import Grid
from day22.node import Node


@pytest.fixture()
def grid2x2():
    nodes = map(Node.from_string, ['/dev/grid/node-x0-y0      93T    0T    93T    76%',
                                   '/dev/grid/node-x1-y0      93T   71T    22T    76%',
                                   '/dev/grid/node-x0-y1      93T   71T    22T    76%',
                                   '/dev/grid/node-x1-y1      93T   71T    22T    76%'])
    return Grid(nodes)


def test_adjacent_nodes(grid2x2):
    assert len(grid2x2._adjacent_nodes(grid2x2.get_node(0, 0))) == 2


def test_has_target_data(grid2x2):
    assert grid2x2.get_node(1, 0).has_target_data


def test_target_data_distance(grid2x2):
    assert grid2x2.target_data_distance == 1


def test_adjacent_grids(grid2x2):
    nodes = map(Node.from_string, ['/dev/grid/node-x0-y0      93T   71T    22T    76%',
                                   '/dev/grid/node-x1-y0      93T    0T    93T    76%',
                                   '/dev/grid/node-x0-y1      93T   71T    22T    76%',
                                   '/dev/grid/node-x1-y1      93T   71T    22T    76%'])
    grid1 = Grid(nodes)
    nodes = map(Node.from_string, ['/dev/grid/node-x0-y0      93T   71T    22T    76%',
                                   '/dev/grid/node-x1-y0      93T   71T    22T    76%',
                                   '/dev/grid/node-x0-y1      93T    0T    93T    76%',
                                   '/dev/grid/node-x1-y1      93T   71T    22T    76%'])
    grid2 = Grid(nodes)

    adjacent_grids = list(grid2x2.adjacent_grids)
    assert grid1 in adjacent_grids
    assert grid2 in adjacent_grids
    assert len(adjacent_grids) == 2
