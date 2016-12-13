class Move:
    def __init__(self, destination_floor, cargo):
        self.destination_floor = destination_floor
        self.cargo = cargo

    def __repr__(self):
        return "Move<%s, %s>" % (self.destination_floor, self.cargo)
