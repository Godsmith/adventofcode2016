from pytest import fixture

from day14.key_generator import KeyGenerator


@fixture
def keygen():
    return KeyGenerator(salt='abc')


def test_contains_triple(keygen):
    assert not keygen.contains_triple(index=17)
    assert keygen.contains_triple(index=18)
