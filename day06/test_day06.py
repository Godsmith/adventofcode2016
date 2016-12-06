import pytest

from day06.day06 import least_frequent_for_each_position
from day06.day06 import most_frequent_for_each_position


@pytest.fixture()
def input_():
    return [s.strip() for s in """eedadn
        drvtee
        eandsr
        raavrd
        atevrs
        tsrnev
        sdttsa
        rasrtv
        nssdts
        ntnada
        svetve
        tesnvt
        vntsnd
        vrdear
        dvrsen
        enarar""".split('\n')]


def test_most_frequent_for_each_position(input_):
    assert most_frequent_for_each_position(input_) == 'easter'


def test_least_frequent_for_each_position(input_):
    assert least_frequent_for_each_position(input_) == 'advent'
