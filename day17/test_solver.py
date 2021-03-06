from day17.solver import Solver


def test_shortest_path():
    assert Solver('ihgpwlah').shortest_path == 'DDRRRD'
    assert Solver('kglvqrro').shortest_path == 'DDUDRLRRUDRD'
    assert Solver('ulqzkmiv').shortest_path == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'


def test_longest_path_length():
    assert Solver('ihgpwlah').longest_path_length == 370
    assert Solver('kglvqrro').longest_path_length == 492
    assert Solver('ulqzkmiv').longest_path_length == 830
