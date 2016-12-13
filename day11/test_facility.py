from day11.facility import Facility
from day11.floor import Floor
from day11.move import Move


def test_to_string():
    facility = Facility([Floor('F1', {'E', 'HM', 'LM'}),
                         Floor('F2', {'HG'}),
                         Floor('F3', {'LG'}),
                         Floor('F4')])
    assert facility.to_string() == ("F4 .  .  .  .  .  \n"
                                    "F3 .  .  .  LG .  \n"
                                    "F2 .  HG .  .  .  \n"
                                    "F1 E  .  HM .  LM \n")


def test_legal():
    facility = Facility([Floor('F1', {'E', 'HM', 'LM'}),
                         Floor('F2', {'HG'}),
                         Floor('F3', {'LG'}),
                         Floor('F4')])
    assert facility.is_legal()

    facility = Facility([Floor('F1', {'E', 'HG', 'HM', 'LM'}),
                         Floor('F2'),
                         Floor('F3', {'LG'}),
                         Floor('F4')])
    assert not facility.is_legal()

    facility = Facility([Floor('F1', {'LM', 'LG', 'HG'}),
                         Floor('F2', {'E', 'HM', }),
                         Floor('F3', {'RG'}),
                         Floor('F4')])
    assert facility.is_legal()


def test_combinations_of_objects():
    assert Facility._combinations_of_objects({'HG', 'HM', 'LG'}) == {frozenset(['HG']), frozenset(['HM']),
                                                                     frozenset(['LG']), frozenset(['HG', 'HM']),
                                                                     frozenset(['HG', 'LG']),
                                                                     frozenset(['HM', 'LG'])}


def test_combination_of_objects_on_current_floor():
    facility = Facility([Floor('F1', {'E', 'HM', 'LM'}),
                         Floor('F2', {'HG'}),
                         Floor('F3', {'LG'}),
                         Floor('F4')])
    assert facility._combinations_of_objects_on_current_floor() == {frozenset(['HM']), frozenset(['LM']),
                                                                    frozenset(['HM', 'LM'])}


def test_adjacent_floors():
    facility = Facility([Floor('F1', {'E', 'HM', 'LM'}),
                         Floor('F2', {'HG'}),
                         Floor('F3', {'LG'}),
                         Floor('F4')])
    assert facility._adjacent_floors() == {'F2'}
    facility = Facility([Floor('F1', {'HM', 'LM'}),
                         Floor('F2', {'E', 'HG'}),
                         Floor('F3', {'LG'}),
                         Floor('F4')])
    assert facility._adjacent_floors() == {'F1', 'F3'}
    facility = Facility([Floor('F1', {'HM', 'LM'}),
                         Floor('F2', {'HG'}),
                         Floor('F3', {'LG'}),
                         Floor('F4', {'E'})])
    assert facility._adjacent_floors() == {'F3'}


def test_create():
    facility = Facility.create([Floor('F1', {'E', 'HM', 'LM'}),
                                Floor('F2', {'HG'}),
                                Floor('F3', {'LG'}),
                                Floor('F4')], [Move('F2', {'HM', 'LM'})])
    assert facility == Facility([Floor('F1'),
                                 Floor('F2', {'E', 'HM', 'LM', 'HG'}),
                                 Floor('F3', {'LG'}),
                                 Floor('F4')])


def test_possible_moves():
    facility = Facility([Floor('F1', {'E', 'HM', 'LM'}),
                         Floor('F2', {'HG'}),
                         Floor('F3', {'LG'}),
                         Floor('F4')])
    assert set(facility.possible_moves()) == {Move('F2', {'HM'})}

    facility = Facility([Floor('F1', {'LM'}),
                         Floor('F2', {'E', 'HG', 'HM', 'LG'}),
                         Floor('F3', {'RG'}),
                         Floor('F4')])
    assert set(facility.possible_moves()) == {Move('F1', {'HM'}), Move('F1', {'LG'}), Move('F1', {'LG', 'HG'}),
                                              Move('F3', {'HG', 'HM'}), Move('F3', {'LG', 'HG'}), Move('F3', {'LG'})}

    facility = Facility([Floor('F1', {'LM'}),
                         Floor('F2', {'E', 'HG', 'HM', 'LG'}),
                         Floor('F3', {'RG'}),
                         Floor('F4')])
    excluded_facility = Facility([Floor('F1', {'E', 'LM', 'HM'}),
                                  Floor('F2', {'HG', 'LG'}),
                                  Floor('F3', {'RG'}),
                                  Floor('F4')])
    assert set(facility.possible_moves(excluded_states={excluded_facility})) == {Move('F1', {'LG'}),
                                                                                 Move('F1', {'LG', 'HG'}),
                                                                                 Move('F3', {'HG', 'HM'}),
                                                                                 Move('F3', {'LG', 'HG'}),
                                                                                 Move('F3', {'LG'})}


def test_is_up():
    facility = Facility([Floor('F1', {'HM', 'LM'}),
                         Floor('F2', {'E', 'HG'}),
                         Floor('F3', {'LG'}),
                         Floor('F4')])
    assert facility.is_up('F3')
    assert not facility.is_up('F2')
    assert not facility.is_up('F1')


def test_all_objects_on_fourth_floor():
    facility = Facility([Floor('F1', {'HM', 'LM'}),
                         Floor('F2', {'E', 'HG'}),
                         Floor('F3', {'LG'}),
                         Floor('F4')])
    assert not facility.all_objects_on_fourth_floor()
    facility = Facility([Floor('F1'),
                         Floor('F2'),
                         Floor('F3'),
                         Floor('F4', {'E', 'LG', 'LM'})])
    assert facility.all_objects_on_fourth_floor()
