from day11.facility import Facility
from day11.move import Move


def test_to_string():
    facility = Facility([{'E', 'HM', 'LM'}, {'HG'}, {'LG'}, set()])
    assert facility.to_string() == ("F4 .  .  .  .  .  \n"
                                    "F3 .  .  .  LG .  \n"
                                    "F2 .  HG .  .  .  \n"
                                    "F1 E  .  HM .  LM \n")


def test_legal():
    facility = Facility([{'E', 'HM', 'LM'}, {'HG'}, {'LG'}, set()])
    assert facility.is_legal()

    facility = Facility([{'E', 'HG', 'HM', 'LM'}, set(), {'LG'}, set()])
    assert not facility.is_legal()

    facility = Facility([{'LM', 'LG', 'HG'}, {'E', 'HM', }, {'RG'}, set()])
    assert facility.is_legal()


def test_combinations_of_objects():
    assert Facility._combinations_of_objects({'HG', 'HM', 'LG'}) == {frozenset(['HG']), frozenset(['HM']),
                                                                     frozenset(['LG']), frozenset(['HG', 'HM']),
                                                                     frozenset(['HG', 'LG']),
                                                                     frozenset(['HM', 'LG'])}


def test_combination_of_objects_on_current_floor():
    facility = Facility([{'E', 'HM', 'LM'}, {'HG'}, {'LG'}, set()])
    assert facility._combinations_of_objects_on_current_floor() == {frozenset(['HM']), frozenset(['LM']),
                                                                    frozenset(['HM', 'LM'])}


def test_adjacent_floors():
    facility = Facility([{'E', 'HM', 'LM'},
                         {'HG'},
                         {'LG'},
                         set()])
    assert facility._adjacent_floors() == {'F2'}
    facility = Facility([{'HM', 'LM'},
                         {'E', 'HG'},
                         {'LG'},
                         set()])
    assert facility._adjacent_floors() == {'F1', 'F3'}
    facility = Facility([{'HM', 'LM'},
                         {'HG'},
                         {'LG'},
                         {'E'}])
    assert facility._adjacent_floors() == {'F3'}


def test_possible_moves():
    facility = Facility([{'E', 'HM', 'LM'},
                         {'HG'},
                         {'LG'},
                         set()])
    assert set(facility.possible_moves()) == {Move('F2', {'HM'})}

    facility = Facility([{'LM'},
                         {'E', 'HG', 'HM', 'LG'},
                         {'RG'},
                         set()])
    assert set(facility.possible_moves()) == {Move('F1', {'HM'}), Move('F1', {'LG'}), Move('F1', {'LG', 'HG'}),
                                              Move('F3', {'HG', 'HM'}), Move('F3', {'LG', 'HG'}), Move('F3', {'LG'})}

    facility = Facility([{'LM'},
                         {'E', 'HG', 'HM', 'LG'},
                         {'RG', 'RM'},
                         set()])
    excluded_facility = Facility([{'E', 'LM', 'HM'},
                                  {'HG', 'LG'},
                                  {'RG', 'RM'},
                                  set()])
    assert set(facility.possible_moves(excluded_states={excluded_facility})) == {Move('F1', {'LG'}),
                                                                                 Move('F1', {'LG', 'HG'}),
                                                                                 Move('F3', {'HG', 'HM'}),
                                                                                 Move('F3', {'LG', 'HG'}),
                                                                                 Move('F3', {'LG'})}


def test_adjacent_states():
    facility = Facility([{'E', 'HM', 'LM'},
                         {'HG'},
                         {'LG'},
                         set()])
    assert set(facility.adjacent_states()) == {
        Facility([{'LM'},
                  {'E', 'HG', 'HM'},
                  {'LG'},
                  set()])}


def test_is_up():
    facility = Facility([{'HM', 'LM'},
                         {'E', 'HG'},
                         {'LG'},
                         set()])
    assert facility.is_up('F3')
    assert not facility.is_up('F2')
    assert not facility.is_up('F1')


def test_all_objects_on_fourth_floor():
    facility = Facility([{'HM', 'LM'},
                         {'E', 'HG'},
                         {'LG'},
                         set()])
    assert not facility.all_objects_on_fourth_floor()
    facility = Facility([set(),
                         set(),
                         set(),
                         {'E', 'LG', 'LM'}])
    assert facility.all_objects_on_fourth_floor()


def test_elements():
    facility = Facility([{'HM', 'LM'},
                         {'E', 'HG'},
                         {'LG'},
                         set()])
    assert facility._elements == ['H', 'L']


def test_translated():
    facility = Facility([{'HM', 'LM'},
                         {'E', 'HG'},
                         {'LG'},
                         set()])
    assert facility.translated({'H': 'L', 'L': 'H'}) == Facility([{'LM', 'HM'}, {'E', 'LG'}, {'HG'}, set()])


def test_permutations():
    facility = Facility([{'HM', 'LM'},
                         {'E', 'HG'},
                         {'LG'},
                         set()])

    assert facility.permutations == {facility, Facility([{'HM', 'LM'}, {'E', 'LG'}, {'HG'}, set()])}
