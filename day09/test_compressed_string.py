from day09.compressed_string import CompressedString


def test_text_inside_parentheses():
    s = CompressedString('A(1x5)BC')
    assert s._text_inside_parentheses(1) == '1x5'
    s = CompressedString('AB(11x25)BC')
    assert s._text_inside_parentheses(2) == '11x25'


def test_text_after_parentheses():
    s = CompressedString('A(1x5)BC')
    assert s._text_after_parentheses(1, 1) == 'B'
    s = CompressedString('AB(11x25)BC')
    assert s._text_after_parentheses(2, 2) == 'BC'


def test_parenthesis_command_text_and_next_index():
    s = CompressedString('A(1x5)BC')
    assert s._parenthesis_command_text_and_next_index(1) == ('BBBBB', 7)
    s = CompressedString('AB(2x2)BC')
    assert s._parenthesis_command_text_and_next_index(2) == ('BCBC', 9)


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
