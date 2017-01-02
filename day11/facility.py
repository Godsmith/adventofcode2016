from copy import deepcopy
from itertools import chain
from itertools import combinations

from day11.floor import Floor
from day11.move import Move

flatten = chain.from_iterable


class Facility:
    floors = ['F1', 'F2', 'F3', 'F4']

    def __init__(self, initial_state):
        self._floors = [Floor('F' + str(i), items) for i, items in enumerate(initial_state, start=1)]

    @classmethod
    def create(cls, initial_state, moves=None):
        if moves is None:
            moves = []
        facility = Facility(initial_state)
        for move in moves:
            facility._move(move)
        return facility

    def __repr__(self):
        return repr(self._floors)

    def __eq__(self, other):
        return type(self) == type(other) and self._floors == other._floors  # self._locations == other._locations

    def __str__(self):
        return '\n'.join([str(floor) for floor in self._floors])

    def __hash__(self):
        return hash(self.to_string())  # hash(tuple(self._floors))

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

    def adjacent_states(self, excluded_states=None):
        if excluded_states is None:
            excluded_states = []
        for floor in self._adjacent_floors():
            for objects in self._combinations_of_objects_on_current_floor():
                move = Move(floor, objects)
                new_facility = deepcopy(self)
                new_facility._move(move)
                if new_facility.is_legal() and new_facility not in excluded_states:
                    yield new_facility

    def possible_moves(self, excluded_states=None):
        if excluded_states is None:
            excluded_states = []
        for floor in self._adjacent_floors():
            for objects in self._combinations_of_objects_on_current_floor():
                move = Move(floor, objects)
                new_facility = deepcopy(self)
                new_facility._move(move)
                if new_facility.is_legal() and new_facility not in excluded_states:
                    yield move

    def _move(self, move: Move):
        self._floors[self._current_floor_index()] = self._current_floor().without(move.cargo.union({'E'}))
        destination_floor_id = self._index_of_floor_with_id(move.destination_floor)
        new_destination_floor = self._floors[destination_floor_id].including(move.cargo.union({'E'}))
        self._floors[destination_floor_id] = new_destination_floor

    def is_legal(self):
        floors_are_legal = [floor.is_legal() for floor in self._floors]
        return not (False in floors_are_legal)

    def is_up(self, destination_floor_id):
        return destination_floor_id > self._current_floor_id()

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

    def all_objects_on_fourth_floor(self):
        return sum([len(f) for f in self._floors[:3]]) == 0

    @property
    def _locations(self):
        # Another way of representing the locations of the items
        items = {}
        types = set()
        for floor in self._floors:
            for item in floor.objects:
                if item == 'E':
                    locations = (int(floor.id[1]), set())  # here the output object is created
                else:
                    items[item] = int(floor.id[1])
                    types.add(item[0])
        for type in types:
            locations[1].add((items[type + 'M'], items[type + 'G']))
        return locations
