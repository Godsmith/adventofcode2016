class Solver:
    def __init__(self, grid):
        self._grid = grid

    def fewest_amount_of_steps(self):
        shortest_data_distance = 999
        grids_to_evaluate = [self._grid]
        evaluated_grids = set()
        steps = 0

        while True:
            grids_to_evaluate_next = set()
            for grid in grids_to_evaluate:
                if grid.target_data_distance < shortest_data_distance:
                    shortest_data_distance = grid.target_data_distance
                if grid.target_data_distance == 0:
                    return steps
                grids_to_evaluate_next.update(grid.adjacent_grids)
                evaluated_grids.add(grid)
            grids_to_evaluate = grids_to_evaluate_next.difference(evaluated_grids)
            print('Step %s. Current shortest distance: %s. Grids to evaluate next: %s' % (
                steps, shortest_data_distance, len(grids_to_evaluate)))
            steps += 1
