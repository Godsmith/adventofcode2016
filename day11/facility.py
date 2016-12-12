from itertools import chain
from itertools import combinations

from day11.floor import Floor
from day11.move import Move

flatten = chain.from_iterable


class Facility:
    floors = ['F1', 'F2', 'F3', 'F4']

    def __init__(self, state, moves=None):
        if moves is None:
            moves = []
        self._state = {floor: Floor(objects) for floor, objects in state.items()}
        for move in moves:
            self._move(move)

    def to_string(self):
        objects = sorted(flatten([floor.objects for floor in self._state.values()]))
        out = []
        for floor in reversed(self.floors):
            out.append(floor + ' ')
            for object in objects:
                if object in self._state[floor].objects:
                    string = object
                else:
                    string = '.'
                out.append(string.ljust(3))
            out.append('\n')
        return ''.join(out)

    def _move(self, move: Move):
        self._state[self._current_floor_id()] = self._current_floor().without(move.cargo.union({'E'}))
        self._state[move.destination_floor] = self._state[move.destination_floor].including(move.cargo.union({'E'}))
        new_facility = Facility(self._state)
        return new_facility

    def is_legal(self):
        return not (False in [floor.is_legal() for floor in self._state.values()])

    def _adjacent_floors(self):
        current_floor_id = self._current_floor_id()
        if current_floor_id == self.floors[0]:
            return {self.floors[1]}
        elif current_floor_id == self.floors[-1]:
            return {self.floors[-2]}
        else:
            index = self.floors.index(current_floor_id)
            return {self.floors[index - 1], self.floors[index + 1]}

    def _combinations_of_objects_on_current_floor(self):
        objects_including_elevator = self._current_floor().objects
        non_elevator_objects = objects_including_elevator.difference({'E'})
        return self._combinations_of_objects(non_elevator_objects)

    def _current_floor(self) -> Floor:
        for floor in self._state.values():
            if 'E' in floor.objects:
                return floor

    def _current_floor_id(self) -> Floor:
        for id, floor in self._state.items():
            if 'E' in floor.objects:
                return id

    @staticmethod
    def _combinations_of_objects(objects: set):
        return {frozenset([o]) for o in objects}.union({frozenset(c) for c in combinations(objects, 2)})
