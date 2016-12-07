from itertools import chain

flatten = chain.from_iterable

class Ipv7String:
    def __init__(self, string):
        self.string = string
        strings_to_the_left_of_brackets = string.split('[')
        self._strings_outside_brackets = [s.split(']')[-1] for s in strings_to_the_left_of_brackets]
        self._strings_inside_brackets = [s.split(']')[0] for s in strings_to_the_left_of_brackets][1:]

        self._abas_outside_brackets = flatten(self._abas(s) for s in self._strings_outside_brackets)
        self._abas_inside_brackets = flatten(self._abas(s) for s in self._strings_inside_brackets)

    def _contains_abba_outside_brackets(self):
        return any([self._contains_abba(s) for s in self._strings_outside_brackets])

    def _contains_abba_inside_brackets(self):
        return any([self._contains_abba(s) for s in self._strings_inside_brackets])

    @staticmethod
    def _contains_abba(s):
        for i in range(len(s) - 3):
            substring = s[i:i + 4]
            if substring[:2] == substring[2:][::-1] and substring[:2] != substring[2:]:
                return True
        return False

    @staticmethod
    def _abas(s):
        for i in range(len(s) - 2):
            substring = s[i:i + 3]
            if substring[0] == substring[2] and substring[0] != substring[1]:
                yield substring
        return False

    @staticmethod
    def _invert_aba(s):
        return ''.join([s[1], s[0], s[1]])

    def supports_tls(self):
        return self._contains_abba_outside_brackets() and not self._contains_abba_inside_brackets()

    def supports_ssl(self):
        for aba in self._abas_outside_brackets:
            if any([self._invert_aba(aba) in s for s in self._strings_inside_brackets]):
                return True
        return False
