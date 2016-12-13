from day11.facility import Facility
from day11.floor import Floor


def main():
    initial_state = [Floor('F1', {'E', 'SG', 'SM', 'PG', 'PM'}),
                     Floor('F2', {'TG', 'RG', 'RM', 'CG', 'CM'}),
                     Floor('F3', {'TM'}),
                     Floor('F4')]
    facility = Facility(initial_state)
    moves = []
    manual = False
    while True:
        print()
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
        else:
            move = best_move(possible_moves, facility)
            moves.append(move)
            print('Selected move: %s. Total moves: %s' % (move, len(moves)))

        facility = Facility.create(initial_state, moves)


def best_move(moves, facility):
    for move in moves:
        if len(move) == 2 and facility.is_up(move.destination_floor):
            return move
    for move in moves:
        if len(move) == 1 and not facility.is_up(move.destination_floor):
            return move
    raise ValueError('No good moves in %s for facility \n%s' % (moves, facility))


if __name__ == '__main__':
    main()
