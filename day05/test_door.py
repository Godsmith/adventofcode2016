import pytest

from day05.door import Door


@pytest.fixture()
def door():
    return Door('abc')


def test_hash(door):
    assert door.hash(3231929)[:5] == '00000'
    assert door.hash(5017308)[:5] == '00000'


def test_hash_indicates_next_character_in_password(door):
    assert door.hash_indicates_next_character_in_password(3231929)
    assert not door.hash_indicates_next_character_in_password(3231928)


def test_password_character(door):
    assert door.password_character(3231929) == '1'


# def test_password(door):
#    assert door.password() == '18f47a30'

def test_advanced_password_character_location(door):
    assert door.advanced_password_character_location(3231929) == '1'
    assert door.advanced_password_character_location(5278568) == 'f'


def test_advanced_password(door):
    assert door.advanced_password == [None] * 8


class TestTryInsertInAdvancedPassword():
    def test_success(self, door):
        door.try_insert_in_advanced_password(3231929)
        assert door.advanced_password[1] == '5'

    def test_invalid_position(self, door):
        door.try_insert_in_advanced_password(5017308)
        assert door.advanced_password == [None] * 8

    def test_invalid_hash(self, door):
        door.try_insert_in_advanced_password(5017309)
        assert door.advanced_password == [None] * 8


def test_generate_advanced_password(door):
    assert door.generate_advanced_password() == '05ace8e3'
