from pytest import fixture

from day14.key_generator import KeyGenerator


@fixture
def keygen():
    return KeyGenerator(salt='abc')


def test_contains_triple(keygen):
    assert keygen.contains_triple(index=17) == (False, None)
    assert keygen.contains_triple(index=18) == (True, '8')


def test_string_contains_sequence(keygen):
    assert (True, '8') == keygen._string_contains_sequence('88888', 5, '8')
    assert (True, '8') == keygen._string_contains_sequence('a88888f', 5, '8')
    assert (False, None) == keygen._string_contains_sequence('a8888f', 5, '8')


def test_is_key_failure(keygen):
    assert not keygen.is_key(index=17)
    assert not keygen.is_key(index=18)


def test_is_key_success(keygen):
    assert keygen.is_key(index=39)
