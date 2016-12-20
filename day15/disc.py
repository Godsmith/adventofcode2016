class Disc:
    @classmethod
    def from_string(cls, s):
        list_ = s.split(' ')
        location = int(list_[1][1])
        positions = int(list_[3])
        starting_position = int(list_[11][:-1])
        return Disc(location, positions, starting_position)

    def __init__(self, location, positions, starting_position):
        self.location = location
        self._positions = positions
        self._position = starting_position

    def tick(self):
        self._position = (self._position + 1) % self._positions

    @property
    def open(self):
        return self._position == 0
