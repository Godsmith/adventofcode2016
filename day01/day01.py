class Agent():
    directions = ['N', 'E', 'S', 'W']
    turn_to_direction = {'N': {'R': 'E', 'L': 'W'},
                         'S': {'L': 'E', 'R': 'W'},
                         'E': {'R': 'S', 'L': 'N'},
                         'W': {'R': 'N', 'L': 'S'}}
    walk_deltas = {'N': (0, -1),
                   'S': (0, 1),
                   'E': (1, 0),
                   'W': (-1, 0)}

    def __init__(self):
        self.direction = 'N'
        self.location = (0, 0)
        self.locations = set()
        self.first_location_visited_twice = None

    def turn(self, dir):
        self.direction = Agent.turn_to_direction[self.direction][dir]

    def walk(self, steps):
        for _ in range(steps):
            self.location = tuple([self.location[i] + Agent.walk_deltas[self.direction][i] for i in [0, 1]])
            if self.first_location_visited_twice is None and self.location in self.locations:
                self.first_location_visited_twice = self.location
            self.locations.add(self.location)

    def move(self, code):
        turn_direction = code[0]
        self.turn(turn_direction)
        steps = int(code[1:])
        self.walk(steps)

    def move_all(self, list_):
        for code in list_:
            self.move(code)

    def distance(self):
        return abs(self.location[0]) + abs(self.location[1])

    def distance_to_first_location_visited_twice(self):
        return abs(self.first_location_visited_twice[0]) + abs(self.first_location_visited_twice[1])


def test_visited_twice_distance():
    agent = Agent()
    agent.walk(2)
    assert (0, -1) in agent.locations
    assert (0, -2) in agent.locations

    agent = Agent()
    agent.move_all(['R8', 'R4', 'R4', 'R8'])
    assert agent.distance_to_first_location_visited_twice() == 4


def test_move():
    agent = Agent()
    agent.move('R2')
    assert agent.location == (2, 0)

    agent = Agent()
    agent.move('L100')
    assert agent.location == (-100, 0)


def test_turn():
    agent = Agent()
    agent.turn('R')
    assert agent.direction == 'E'

    agent = Agent()
    agent.turn('L')
    assert agent.direction == 'W'

    agent = Agent()
    agent.turn('L')
    agent.turn('L')
    agent.turn('L')
    agent.turn('L')
    assert agent.direction == 'N'


def test_walk():
    agent = Agent()
    agent.walk(2)
    assert agent.distance() == 2

    agent = Agent()
    agent.walk(2)
    agent.turn('L')
    agent.walk(3)
    assert agent.distance() == 5


def test_starting_direction():
    agent = Agent()
    assert agent.direction == 'N'


def test_move_all():
    agent = Agent()
    agent.move_all(['R2', 'L3'])
    assert agent.distance() == 5

    agent = Agent()
    agent.move_all(['R2', 'R2', 'R2'])
    assert agent.distance() == 2

    agent = Agent()
    agent.move_all(['R5', 'L5', 'R5', 'R3'])
    assert agent.distance() == 12


input_ = 'L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2'
input_list = input_.split(', ')
agent = Agent()
agent.move_all(input_list)
print(agent.distance())
print(agent.distance_to_first_location_visited_twice())
