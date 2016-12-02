from day02 import Keypad, StarKeypad


class TestKeypad:
    def test_add_tuples(self):
        assert Keypad._add_lists([1, 3], [2, 4]) == [3, 7]

    def test_start_location(self):
        keypad = Keypad()
        assert keypad.current_digit == '5'

    def test_move(self):
        keypad = Keypad()
        keypad.move_finger('U')
        assert keypad.current_digit == '2'

        keypad = Keypad()
        keypad.move_finger('R')
        assert keypad.current_digit == '6'

    def test_move_outside(self):
        keypad = Keypad()
        keypad.move_finger('U')
        keypad.move_finger('U')
        assert keypad.current_digit == '2'

        keypad.move_finger('L')
        keypad.move_finger('L')
        assert keypad.current_digit == '1'

    def test_move_all(self):
        keypad = Keypad()
        keypad.move_all('UU')
        assert keypad.current_digit == '2'

        keypad = Keypad()
        keypad.move_all('UDLR')
        assert keypad.current_digit == '5'

    def test_to_code(self):
        keypad = Keypad()
        assert keypad.to_code(['ULL', 'RRDDD', 'LURDL', 'UUUUD']) == '1985'


class TestStarKeypad:
    def test_move(self):
        keypad = StarKeypad()
        keypad.move_finger('R')
        assert keypad.current_digit == '6'

    def test_move_outside(self):
        keypad = StarKeypad()
        keypad.move_finger('L')
        assert keypad.current_digit == '5'
        keypad.move_finger('D')
        assert keypad.current_digit == '5'
        keypad.move_finger('U')
        assert keypad.current_digit == '5'
        keypad.move_finger('R')
        keypad.move_finger('U')
        keypad.move_finger('U')
        assert keypad.current_digit == '2'
        keypad.move_finger('R')
        keypad.move_finger('D')
        keypad.move_finger('D')
        keypad.move_finger('D')
        keypad.move_finger('D')
        assert keypad.current_digit == 'D'

    def test_to_code(self):
        keypad = StarKeypad()
        assert keypad.to_code(['ULL', 'RRDDD', 'LURDL', 'UUUUD']) == '5DB3'
