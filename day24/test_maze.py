from pytest import fixture

from day24.maze import Maze, Point


@fixture
def maze1():
    s = """
    ###########
    #0.1.....2#
    #.#######.#
    #4.......3#
    ###########
    """
    return Maze([line.strip() for line in s.split('\n')][1:-1])


def test_is_wall(maze1):
    assert maze1._is_wall(Point(0, 0))
    assert not maze1._is_wall(Point(1, 1))
    assert not maze1._is_wall(Point(1, 2))


def test_find_coordinates(maze1):
    assert maze1._find_coordinates('0') == Point(1, 1)


def test_shortest(maze1):
    assert maze1.shortest_route_length(0, 1) == 2
    assert maze1.shortest_route_length(0, 3) == 10
    #
    # def test_shortest():
    #     with open('input.txt') as f:
    #         maze = [line[:-1] for line in f.readlines()]
    #         assert Maze(maze).shortest_route_length(0, 1) == 22
