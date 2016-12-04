from day04 import Room


def test_code():
    r = Room('aaaaa-bbb-z-y-x-123[abxyz]')
    assert r.code == 'aaaaa-bbb-z-y-x-123[abxyz]'


def test_encrypted_name():
    r = Room('aaaaa-bbb-z-y-x-123[abxyz]')
    assert r.encrypted_name == 'aaaaa-bbb-z-y-x'


def test_precalculated_checksum():
    r = Room('aaaaa-bbb-z-y-x-123[abxyz]')
    assert r.precalculated_checksum == 'abxyz'
    r = Room('aaaaa-bbb-z-y-x-123[abxyz]\n')
    assert r.precalculated_checksum == 'abxyz'


def test_calculate_checksum():
    r = Room('aaaaa-bbb-z-y-x-123[abxyz]')
    assert r.calculate_checksum() == 'abxyz'


def test_is_real():
    r = Room('aaaaa-bbb-z-y-x-123[abxyz]')
    assert r.is_real()
    r = Room('a-b-c-d-e-f-g-h-987[abcde]')
    assert r.is_real()
    r = Room('not-a-real-room-404[oarel]')
    assert r.is_real()
    r = Room('totally-real-room-200[decoy]')
    assert not r.is_real()


def test_sector_id():
    r = Room('aaaaa-bbb-z-y-x-123[abxyz]')
    assert r.sector_id == 123
