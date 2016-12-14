from day12.computer import Computer

with open('input.txt') as f:
    instructions = [s.strip() for s in f.readlines()]
    computer = Computer()
    computer.registers['c'] = 1
    computer.evaluate(instructions)
    print(computer.register('a'))
