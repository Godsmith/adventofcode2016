from day11.floor import Floor
from day11.solver import Solver


class NoGoodMovesException(Exception):
    pass


def main():
    initial_state = [Floor('F1', {'E', 'SG', 'SM', 'PG', 'PM'}),
                     Floor('F2', {'TG', 'RG', 'RM', 'CG', 'CM'}),
                     Floor('F3', {'TM'}),
                     Floor('F4')]
    # initial_state = [Floor('F1', {'E', 'EG', 'EM', 'DG', 'DM', 'SG', 'SM', 'PG', 'PM'}),
    #                  Floor('F2', {'TG', 'RG', 'RM', 'CG', 'CM'}),
    #                  Floor('F3', {'TM'}),
    #                  Floor('F4')]

    print(Solver(initial_state).solve())





def best_move(moves, facility):
    for move in moves:
        if len(move) == 2 and facility.is_up(move.destination_floor):
            return move
    for move in moves:
        if len(move) == 1 and not facility.is_up(move.destination_floor):
            return move
    raise NoGoodMovesException()


if __name__ == '__main__':
    main()
