from day12.computer import Computer


def test_evaluate():
    instructions = [s.strip() for s in """cpy 41 a
    inc a
    inc a
    dec a
    jnz a 2
    dec a""".split('\n')]
    computer = Computer()
    computer.evaluate(instructions)
    assert computer.register('a') == 42


def test_evaluate_tgl():
    instructions = [s.strip() for s in """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a""".split('\n')]
    computer = Computer()
    computer.evaluate(instructions)
    assert computer.register('a') == 3


def test_output():
    instructions = [s.strip() for s in """cpy 2 a
out a""".split('\n')]
    computer = Computer()
    assert next(computer.output(instructions)) == 0
