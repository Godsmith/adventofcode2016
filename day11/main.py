from day11.solver import Solver


class NoGoodMovesException(Exception):
    pass


def main():
    initial_state = [{'E', 'SG', 'SM', 'PG', 'PM'},
                     {'TG', 'RG', 'RM', 'CG', 'CM'},
                     {'TM'},
                     set()]
    initial_state = [{'E', 'EG', 'EM', 'DG', 'DM', 'SG', 'SM', 'PG', 'PM'},
                     {'TG', 'RG', 'RM', 'CG', 'CM'},
                     {'TM'},
                     set()]

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
