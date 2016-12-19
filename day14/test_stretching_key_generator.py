from pytest import fixture

from day14.stretching_key_generator import StretchingKeyGenerator


@fixture
def keygen():
    return StretchingKeyGenerator('abc')


def test_md5(keygen):
    assert keygen._md5(0) == 'a107ff634856bb300138cac6568c0f24'


def test_index_of_nth_key(keygen):
    assert keygen.index_of_nth_key(1) == 10
    assert keygen.index_of_nth_key(64) == 22551
