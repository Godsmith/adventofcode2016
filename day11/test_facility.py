from day11.facility import Facility
from day11.move import Move


def test_to_string():
    facility = Facility({'F1': {'E', 'HM', 'LM'},
                         'F2': {'HG'},
                         'F3': {'LG'},
                         'F4': set()})
    assert facility.to_string() == ("F4 .  .  .  .  .  \n"
                                    "F3 .  .  .  LG .  \n"
                                    "F2 .  HG .  .  .  \n"
                                    "F1 E  .  HM .  LM \n")


def test_legal():
    facility = Facility({'F1': {'E', 'HM', 'LM'},
                         'F2': {'HG'},
                         'F3': {'LG'},
                         'F4': set()})
    assert facility.is_legal()

    facility = Facility({'F1': {'E', 'HG', 'HM', 'LM'},
                         'F2': set(),
                         'F3': {'LG'},
                         'F4': set()})
    assert not facility.is_legal()


def test_combinations_of_objects():
    assert Facility._combinations_of_objects({'HG', 'HM', 'LG'}) == {frozenset(['HG']), frozenset(['HM']),
                                                                     frozenset(['LG']), frozenset(['HG', 'HM']),
                                                                     frozenset(['HG', 'LG']),
                                                                     frozenset(['HM', 'LG'])}


def test_combination_of_objects_on_current_floor():
    facility = Facility({'F1': {'E', 'HM', 'LM'},
                         'F2': {'HG'},
                         'F3': {'LG'},
                         'F4': set()})
    assert facility._combinations_of_objects_on_current_floor() == {frozenset(['HM']), frozenset(['LM']),
                                                                    frozenset(['HM', 'LM'])}


def test_adjacent_floors():
    facility = Facility({'F1': {'E', 'HM', 'LM'},
                         'F2': {'HG'},
                         'F3': {'LG'},
                         'F4': set()})
    assert facility._adjacent_floors() == {'F2'}
    facility = Facility({'F1': {'HM', 'LM'},
                         'F2': {'E', 'HG'},
                         'F3': {'LG'},
                         'F4': set()})
    assert facility._adjacent_floors() == {'F1', 'F3'}
    facility = Facility({'F1': {'HM', 'LM'},
                         'F2': {'HG'},
                         'F3': {'LG'},
                         'F4': {'E'}})
    assert facility._adjacent_floors() == {'F3'}


def test_move():
    facility = Facility({'F1': {'E', 'HM', 'LM'},
                         'F2': {'HG'},
                         'F3': {'LG'},
                         'F4': set()}, [Move('F2', {'HM', 'LM'})])
    facility2 = facility._move(Move('F2', {'HM', 'LM'}))
    assert facility2 == Facility({'F1': set(),
                                  'F2': {'E', 'HM', 'LM', 'HG'},
                                  'F3': {'LG'},
                                  'F4': set()})


def test_possible_moves():
    facility = Facility({'F1': {'E', 'HM', 'LM'},
                         'F2': {'HG'},
                         'F3': {'LG'},
                         'F4': set()})
    assert facility.possible_moves() == {Move('F2', 'HM')}
