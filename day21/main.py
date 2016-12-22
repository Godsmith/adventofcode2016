from day21.scrambler import Scrambler

with open('input.txt') as f:
    operations = f.readlines()
    print(Scrambler.do_all(operations, 'abcdefgh'))