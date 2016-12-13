from itertools import chain
from itertools import combinations

from day11.floor import Floor
from day11.move import Move

flatten = chain.from_iterable


class Facility:
    floors = ['F1', 'F2', 'F3', 'F4']

    def __init__(self, floors, moves=None):
        if moves is None:
            moves = []
        self._floors = floors
        self._moves = moves
        for move in moves:
            self._move(move)

    def __repr__(self):
        return repr(self._floors)

    def __eq__(self, other):
        return type(self) == type(other) and self._floors == other._floors


    def to_string(self):
        objects = sorted(flatten([floor.objects for floor in self._floors]))
        out = []
        for floor_id in reversed(self.floors):
            out.append(floor_id + ' ')
            for object in objects:
                if object in [floor for floor in self._floors if floor.id == floor_id][0].objects:
                    string = object
                else:
                    string = '.'
                out.append(string.ljust(3))
            out.append('\n')
        return ''.join(out)

    def possible_moves(self):
        for floor in self._adjacent_floors():
            for objects in self._combinations_of_objects_on_current_floor():
                yield Move(floor, objects)

    def _move(self, move: Move):
        self._floors[self._current_floor_index()] = self._current_floor().without(move.cargo.union({'E'}))
        destination_floor_id = self._index_of_floor_with_id(move.destination_floor)
        new_destination_floor = self._floors[destination_floor_id].including(move.cargo.union({'E'}))
        self._floors[destination_floor_id] = new_destination_floor

    def is_legal(self):
        return not (False in [floor.is_legal() for floor in self._floors])

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
        return next(filter(lambda f: 'E' in f.objects, self._floors))

    def _current_floor_id(self) -> Floor:
        for floor in self._floors:
            if 'E' in floor.objects:
                return floor.id

    def _current_floor_index(self):
        for i, floor in enumerate(self._floors):
            if 'E' in floor.objects:
                return i

    def _index_of_floor_with_id(self, id):
        for i, floor in enumerate(self._floors):
            if floor.id == id:
                return i

    @staticmethod
    def _combinations_of_objects(objects: set):
        return {frozenset([o]) for o in objects}.union({frozenset(c) for c in combinations(objects, 2)})
