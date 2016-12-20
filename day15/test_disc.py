from pytest import fixture

from day15.disc import Disc


@fixture
def disc1():
    return Disc.from_string('Disc #1 has 5 positions; at time=0, it is at position 4.')


def test_create(disc1):
    assert disc1.location == 1
    assert not disc1.open
    disc1.tick()
    assert disc1.open
