import itertools

from day12.computer import Computer

NUMBER_OF_ELEMENTS_TO_CHECK = 10

with open('input.txt') as f:
    instructions = [s.strip() for s in f.readlines()]
    for i in range(1000):
        computer = Computer()
        computer.registers['a'] = i
        first_elements = list(itertools.islice(computer.output(list(instructions)), NUMBER_OF_ELEMENTS_TO_CHECK))
        if first_elements == [0, 1] * int(NUMBER_OF_ELEMENTS_TO_CHECK / 2):
            print(i)
