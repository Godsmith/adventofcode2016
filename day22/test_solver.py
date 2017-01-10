import pytest

from day22.grid import Grid
from day22.node import Node
from day22.solver import Solver


@pytest.fixture()
def grid2x2():
    nodes = map(Node.from_string, ['/dev/grid/node-x0-y0      93T    0T    93T    76%',
                                   '/dev/grid/node-x1-y0      93T   71T    22T    76%',
                                   '/dev/grid/node-x0-y1      93T   71T    22T    76%',
                                   '/dev/grid/node-x1-y1      93T   71T    22T    76%'])
    return Grid(nodes)


@pytest.fixture()
def grid2x2harder():
    nodes = map(Node.from_string, ['/dev/grid/node-x0-y0      93T   71T    22T    76%',
                                   '/dev/grid/node-x1-y0      93T   71T    22T    76%',
                                   '/dev/grid/node-x0-y1      93T   71T    22T    76%',
                                   '/dev/grid/node-x1-y1      93T    0T    93T    76%'])
    return Grid(nodes)


def test_fewest_amount_of_steps(grid2x2, grid2x2harder):
    solver = Solver(grid2x2)
    assert solver.fewest_amount_of_steps() == 1

    solver = Solver(grid2x2harder)
    assert solver.fewest_amount_of_steps() == 3
