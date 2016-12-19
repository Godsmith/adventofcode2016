import hashlib


class KeyGenerator:
    def __init__(self, salt):
        self._salt = salt.encode('utf-8')

    def contains_triple(self, index):
        m = hashlib.md5()
        m.update(self._salt)
        m.update(str(index).encode('utf-8'))
        s = m.hexdigest()
        return self._string_contains_triple(s)

    @staticmethod
    def _string_contains_triple(s):
        for i, c in enumerate(s[:-2]):
            if c == s[i + 1] == s[i + 2]:
                return True
        return False
