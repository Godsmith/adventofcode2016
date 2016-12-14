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