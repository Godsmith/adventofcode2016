from day17.maze import Maze


def test_possible_moves():
    assert Maze(passcode='hijkl', room=(0, 0), path='').adjacent_states == [
        Maze(passcode='hijkl', room=(0, 1), path='D')]
