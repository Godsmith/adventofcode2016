import hashlib


class KeyGenerator:
    def __init__(self, salt):
        self._salt = salt.encode('utf-8')

    def contains_triple(self, index):
        return self._string_contains_triple(self._md5(index))

    def is_key(self, index):
        success, character = self.contains_triple(index)
        if not success:
            return False
        return self._five_characters_in_a_row_in_next_thousand_indices(index, character)

    def _five_characters_in_a_row_in_next_thousand_indices(self, index, c):
        for i in range(index + 1, index + 1001):
            md5 = self._md5(i)
            success, _ = self._string_contains_sequence(md5, 5, character=c)
            if success:
                return True
        return False

    def _md5(self, index):
        m = hashlib.md5()
        m.update(self._salt)
        m.update(str(index).encode('utf-8'))
        return m.hexdigest()

    @classmethod
    def _string_contains_triple(cls, s):
        return cls._string_contains_sequence(s, 3)

    @classmethod
    def _string_contains_sequence(cls, s, n, character=None):
        for i, c in enumerate(s[:-2]):
            if len(set(s[i:i + n])) == 1:
                if character is None:
                    return True, c
                elif character == c:
                    return True, c
        return False, None
