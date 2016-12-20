from day17.solver import Solver


def test_shortest_path():
    assert Solver('ihgpwlah').shortest_path == 'DDRRRD'
    assert Solver('kglvqrro').shortest_path == 'DDUDRLRRUDRD'
    assert Solver('ulqzkmiv').shortest_path == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
