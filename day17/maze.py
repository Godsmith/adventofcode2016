import hashlib

from day17.move import Move


class Maze:
    OPEN_LETTERS = ['b', 'c', 'd', 'e', 'f']
    DIRECTIONS = ['U', 'D', 'L', 'R']

    def __init__(self, passcode, room, path):
        self._passcode = passcode
        self._room = room
        self._path = path

    def __repr__(self):
        return 'Maze<' + repr(self._room) + ' ' + repr(self._path) + '>'

    def __eq__(self, other):
        return self._passcode == other._passcode and self._room == other._room and self._path == other._path

    @property
    def adjacent_states(self):
        m = hashlib.md5()
        m.update(self._passcode.encode('utf-8'))
        m.update(self._path.encode('utf-8'))
        md5 = m.hexdigest()
        adjacent_mazes = [Maze(self._passcode, move.target_room, self._path + move.direction) for move in
                          self._possible_moves(md5)]
        return adjacent_mazes

    def _possible_moves(self, md5):
        x = self._room[0]
        y = self._room[1]
        new_rooms = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        possible_moves = [Move(direction, r) for direction, r, c in zip(self.DIRECTIONS, new_rooms, md5) if
                          direction in self.DIRECTIONS and c in self.OPEN_LETTERS and r[0] >= 0 and r[1] >= 0 and r[
                              0] <= 4 and r[1] <= 4]
        return possible_moves
