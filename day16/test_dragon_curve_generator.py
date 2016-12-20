from day16.dragon_curve_generator import DragonCurveGenerator


def test_step():
    assert DragonCurveGenerator.step('1') == '100'
    assert DragonCurveGenerator.step('0') == '001'
    assert DragonCurveGenerator.step('11111') == '11111000000'
    assert DragonCurveGenerator.step('111100001010') == '1111000010100101011110000'


def test_checksum():
    assert DragonCurveGenerator.checksum('110010110100') == '100'


def test_checksum_of_filled_disk():
    assert DragonCurveGenerator.checksum_of_filled_disk(20, '10000') == '01100'
