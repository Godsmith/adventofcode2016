from day11.floor import Floor
from day11.solver import Solver


# def test_solve_part1():
#     solver = Solver(initial_state=[Floor('F1', {'E', 'SG', 'SM', 'PG', 'PM'}),
#                                    Floor('F2', {'TG', 'RG', 'RM', 'CG', 'CM'}),
#                                    Floor('F3', {'TM'}),
#                                    Floor('F4')])
#     assert solver.solve() == 37

def test_solve_example():
    solver = Solver(initial_state=[Floor('F1', {'E', 'HM', 'LM'}),
                                   Floor('F2', {'HG'}),
                                   Floor('F3', {'LG'}),
                                   Floor('F4')])
    assert solver.solve() == 11


def test_solve_slower():
    # 4s 55 ms
    solver = Solver(initial_state=[Floor('F1', {'E', 'HM', 'LM', 'SM'}),
                                   Floor('F2', {'HG'}),
                                   Floor('F3', {'LG', 'SG'}),
                                   Floor('F4')])
    assert solver.solve() == 23
