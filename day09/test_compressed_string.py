from day09.compressed_string import CompressedString, CompressedString2


def test_text_inside_parentheses():
    s = CompressedString('A(1x5)BC')
    assert s._text_inside_parentheses(1) == '1x5'
    s = CompressedString('AB(2x10)BC')
    assert s._text_inside_parentheses(2) == '2x10'

def test_decompress():
    s = CompressedString('ADVENT')
    assert s.decompressed_length() == 6

    s = CompressedString('A(1x5)BC')
    assert s.decompressed_length() == 7

    s = CompressedString('(3x3)XYZ')
    assert s.decompressed_length() == 9

    s = CompressedString('A(2x2)BCD(2x2)EFG')
    assert s.decompressed_length() == 11

    s = CompressedString('(6x1)(1x3)A')
    assert s.decompressed_length() == 6

    s = CompressedString('X(8x2)(3x3)ABCY')
    assert s.decompressed_length() == 18


def test_multipliers():
    s = CompressedString('ADVENT')
    assert s._multipliers == [1, 1, 1, 1, 1, 1]

    s = CompressedString('A(1x5)BC')
    assert s._multipliers == [1, 0, 0, 0, 0, 0, 5, 1]


def test_decompress_2():
    s = CompressedString2('ADVENT')
    assert s.decompressed_length() == 6

    s = CompressedString2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')
    assert s.decompressed_length() == 445

    s = CompressedString2('A(1x5)BC')
    assert s.decompressed_length() == 7
