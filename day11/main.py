from day11.facility import Facility
from day11.floor import Floor

initial_state = [Floor('F1', {'E', 'SG', 'SM', 'PG', 'PM'}),
                 Floor('F2', {'TG', 'RG', 'RM', 'CG', 'CM'}),
                 Floor('F3', {'TM'}),
                 Floor('F4')]
facility = Facility(initial_state)
moves = []
manual = True
while True:
    print(facility)
    possible_moves = list(facility.possible_moves())
    for i, move in enumerate(possible_moves):
        print('%s: %s' % (i, move))
    if manual:
        ok = False
        while not ok:
            input_ = input('Total moves: %s. Select move: ' % len(moves))
            try:
                moves.append(possible_moves[int(input_)])
                ok = True
            except (IndexError, ValueError):
                print('Invalid input.')
    facility = Facility.create(initial_state, moves)
