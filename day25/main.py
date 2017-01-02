from day12.computer import Computer

with open('input.txt') as f:
    instructions = [s.strip() for s in f.readlines()]
    computer = Computer()
    # computer.registers['a'] = 7
    computer.registers['a'] = 12
    for _ in range(10):
        print(computer.output(instructions))
