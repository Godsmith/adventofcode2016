from day11.solver import Solver


# def test_solve_part1():
#     solver = Solver(initial_state=[Floor('F1', {'E', 'SG', 'SM', 'PG', 'PM'}),
#                                    Floor('F2', {'TG', 'RG', 'RM', 'CG', 'CM'}),
#                                    Floor('F3', {'TM'}),
#                                    Floor('F4')])
#     assert solver.solve() == 37

def test_solve_example():
    solver = Solver(initial_state=[{'E', 'HM', 'LM'}, {'HG'}, {'LG'}, {}])
    assert solver.solve() == 11


def test_solve_slower():
    # 2s 382ms to 3s 427 ms
    solver = Solver(initial_state=[{'E', 'HM', 'LM', 'SM'},
                                   {'HG'},
                                   {'LG', 'SG'}, {}])
    assert solver.solve() == 23
