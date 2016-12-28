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


def test_special_characters(maze1):
    assert maze1._special_characters == {'0', '1', '2', '3', '4'}


def test_fewest_steps_to_visit_all(maze1):
    assert maze1.fewest_steps_to_visit_all() == 14
