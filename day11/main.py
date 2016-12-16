from day11.facility import Facility
from day11.floor import Floor


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
    # moves = []
    # excluded_states = set()
    # while True:
    #     facility = Facility.create(initial_state, moves)
    #     print()
    #     print(facility)
    #     if facility.all_objects_on_fourth_floor():
    #         break
    #     possible_moves = list(facility.possible_moves(excluded_states))
    #     for i, move in enumerate(possible_moves):
    #         print('%s: %s' % (i, move))
    #     try:
    #         move = best_move(possible_moves, facility)
    #         moves.append(move)
    #         print('Selected move: %s. Total moves: %s' % (move, len(moves)))
    #     except NoGoodMovesException:
    #         excluded_states.add(facility)
    #         moves = moves[:-1]
    #         print('No good moves, excluding facility.')

    facilities_to_evaluate_next_step = {Facility.create(initial_state)}
    evaluated_facilities = set()
    moves = 0
    while True:
        print(moves)
        facilities_to_evaluate_this_step = list(facilities_to_evaluate_next_step)
        facilities_to_evaluate_next_step = []

        for facility in facilities_to_evaluate_this_step:
            if facility.all_objects_on_fourth_floor():
                print('solution found')
                return
            adjacent_states_to_current_facility = facility.adjacent_states(evaluated_facilities)
            facilities_to_evaluate_next_step.extend(adjacent_states_to_current_facility)
            evaluated_facilities.add(facility)

        moves += 1



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
