class Agent():
    directions = ['N', 'E', 'S', 'W']

    def __init__(self):
        self.direction = 'N'
        self.x = 0
        self.y = 0

    def turn(self, dir):
        current_direction_index = Agent.directions.index(self.direction)
        if dir == 'R':
            new_direction_index = current_direction_index + 1
        elif dir == 'L':
            new_direction_index = current_direction_index - 1
        else:
            raise ValueError('Direction must be R or L')
        if new_direction_index == 4:
            new_direction_index = 0
        self.direction = Agent.directions[new_direction_index]

    def walk(self, steps):
        if self.direction == 'N':
            self.y -= steps
        elif self.direction == 'S':
            self.y += steps
        elif self.direction == 'E':
            self.x += steps
        elif self.direction == 'W':
            self.x -= steps

    def move(self, code):
        turn_direction = code[0]
        self.turn(turn_direction)
        steps = int(code[1:])
        self.walk(steps)

    def move_all(self, list_):
        for code in list_:
            self.move(code)

    def distance(self):
        return abs(self.x) + abs(self.y)


def test_move():
    agent = Agent()
    agent.move('R2')
    assert agent.x == 2
    assert agent.y == 0

    agent = Agent()
    agent.move('L100')
    assert agent.x == -100
    assert agent.y == 0


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
