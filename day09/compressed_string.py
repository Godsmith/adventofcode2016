class CompressedString():
    def __init__(self, string):
        self._string = string
        self._multipliers = [1] * len(string)
        i = 0
        while i < len(self._string):
            if self._string[i] == '(':
                i = self._set_parenthesis_multiplier_and_return_next_index(i)
            else:
                i += 1

    def _set_parenthesis_multiplier_and_return_next_index(self, starting_parenthesis_index):
        e = self._ending_parenthesis_index(starting_parenthesis_index)
        # Set parenthesis multipliers to 0
        for i in range(starting_parenthesis_index, e + 1):
            self._multipliers[i] = 0

        text = self._text_inside_parentheses(starting_parenthesis_index)
        characters = int(text.split('x')[0])
        times = int(text.split('x')[1])
        for i in range(e + 1, e + 1 + characters):
            self._multipliers[i] *= times
        return e + self._after_parenthesis_offset_multiplier * characters + 1

    def decompressed_length(self):
        return sum(self._multipliers)

    def _text_inside_parentheses(self, starting_parenthesis_index):
        e = self._ending_parenthesis_index(starting_parenthesis_index)
        return self._string[starting_parenthesis_index + 1:e]

    def _ending_parenthesis_index(self, starting_parenthesis_index):
        return self._string.find(')', starting_parenthesis_index)

    @property
    def _after_parenthesis_offset_multiplier(self):
        return 1


class CompressedString2(CompressedString):
    @property
    def _after_parenthesis_offset_multiplier(self):
        return 0
