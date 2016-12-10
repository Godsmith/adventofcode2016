class CompressedString(str):
    def decompressed_length(self):
        length = 0
        i = 0
        while i < len(self):
            c = self[i]

            if c == '(':
                repeated_length, i = self._length_of_parenthesis_command_and_next_index(i)
                length += repeated_length
            else:
                length += 1
                i += 1
        return length

    def _text_inside_parentheses(self, starting_parenthesis_index):
        e = self._ending_parenthesis_index(starting_parenthesis_index)
        return self[starting_parenthesis_index + 1:e]

    def _text_after_parentheses(self, starting_parenthesis_index, characters):
        e = self._ending_parenthesis_index(starting_parenthesis_index)
        return self[e + 1:e + 1 + characters]

    def _ending_parenthesis_index(self, starting_parenthesis_index):
        return self.find(')', starting_parenthesis_index)

    def _length_of_parenthesis_command_and_next_index(self, starting_parenthesis_index):
        text = self._text_inside_parentheses(starting_parenthesis_index)
        characters = int(text.split('x')[0])
        times = int(text.split('x')[1])
        ending_parenthesis_index = self.find(')', starting_parenthesis_index)
        return (
        characters * times, ending_parenthesis_index + self._after_parenthesis_offset_multiplier * characters + 1)

    @property
    def _after_parenthesis_offset_multiplier(self):
        return 1


class CompressedString2(CompressedString):
    @property
    def _after_parenthesis_offset_multiplier(self):
        return 0
