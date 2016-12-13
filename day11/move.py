class Move:
    def __init__(self, destination_floor, cargo):
        self.destination_floor = destination_floor
        self.cargo = cargo

    def __repr__(self):
        return "Move<%s, %s>" % (self.destination_floor, self.cargo)

    def __eq__(self, other):
        return type(self) == type(
            other) and self.destination_floor == other.destination_floor and self.cargo == other.cargo

    def __hash__(self):
        return hash((self.destination_floor, tuple(self.cargo)))
