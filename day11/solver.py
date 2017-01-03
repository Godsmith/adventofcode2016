from day11.facility import Facility


class Solver:
    def __init__(self, initial_state):
        self._initial_state = initial_state

    def solve(self):
        facilities_to_evaluate_next_step = {Facility.create(self._initial_state)}
        evaluated_facilities = set()
        moves = 0
        while True:
            facilities_to_evaluate_this_step = list(facilities_to_evaluate_next_step)
            facilities_to_evaluate_next_step = []
            print('Move: %s' % moves)
            print('Facilities to evaluate this step: %s' % len(facilities_to_evaluate_this_step))

            for facility in facilities_to_evaluate_this_step:
                if facility in evaluated_facilities:
                    continue
                if facility.all_objects_on_fourth_floor():
                    print('Solution found')
                    return moves
                adjacent_states_to_current_facility = facility.adjacent_states()
                facilities_to_evaluate_next_step.extend(adjacent_states_to_current_facility)
                evaluated_facilities.update(facility.permutations)

            moves += 1
