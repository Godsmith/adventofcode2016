from day04.ordered_ignoring_counter import OrderedIgnoringCounter


class Room:
    def __init__(self, code):
        self.code = code
        self.encrypted_name = '-'.join(code.split('[')[0].split('-')[:-1])
        self.precalculated_checksum = code.split('[')[1].split(']')[0]
        self.sector_id = int(code.split('[')[0].split('-')[-1])
        self.real_name = self._shift_string(self.encrypted_name.replace('-', ' '), self.sector_id)

    @staticmethod
    def _shift_letter(letter, steps):
        # a = 97
        # z = 122
        if letter == ' ':
            return ' '
        letter_code_from_0 = ord(letter) - 97
        new_letter_code_from_0 = (letter_code_from_0 + steps) % 26
        return chr(new_letter_code_from_0 + 97)

    def calculate_checksum(self):
        counter = OrderedIgnoringCounter(self.encrypted_name, ignore='-')
        return ''.join([t[0] for t in counter.most_common()])[:5]

    def is_real(self):
        return self.precalculated_checksum == self.calculate_checksum()

    @classmethod
    def _shift_string(cls, s, steps):
        return ''.join([cls._shift_letter(c, steps) for c in s])
