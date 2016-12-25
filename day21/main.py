from day21.scrambler import Scrambler

with open('input.txt') as f:
    operations = [line[:-1] for line in f.readlines() if len(line) > 0]
    print(Scrambler.do_all(operations, 'abcdefgh'))
    print(Scrambler.do_all(operations, 'fbgdceah', reverse=True))
