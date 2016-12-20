from itertools import chain

from day17.maze import Maze

flatten = chain.from_iterable


class Solver:
    def __init__(self, passcode):
        self._passcode = passcode

    @property
    def shortest_path(self):
        states_to_evaluate = [Maze(passcode=self._passcode)]
        while True:
            states_to_evaluate = list(flatten([m.adjacent_states for m in states_to_evaluate]))
            paths_to_finish = [m.path for m in states_to_evaluate if m.room == (3, 3)]
            if len(paths_to_finish) > 0:
                return paths_to_finish[0]

    @property
    def longest_path_length(self):
        states_to_evaluate = [Maze(passcode=self._passcode)]
        steps = 0
        max_steps = 0
        while len(states_to_evaluate) > 0:
            steps += 1
            states_to_evaluate = list(flatten([m.adjacent_states for m in states_to_evaluate]))
            if (3, 3) in [m.room for m in states_to_evaluate]:
                max_steps = steps
            states_to_evaluate = [m for m in states_to_evaluate if m.room != (3, 3)]
        return max_steps


print(Solver('pslxynzg').shortest_path)
print(Solver('pslxynzg').longest_path_length)
