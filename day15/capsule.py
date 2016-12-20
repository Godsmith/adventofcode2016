class Capsule:
    def __init__(self, starting_time):
        self.location = 0
        self.starting_time = starting_time

    def tick(self):
        self.location += 1
