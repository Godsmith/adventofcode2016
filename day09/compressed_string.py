class CompressedString(str):
    def decompressed_length(self):
        decompressed = []
        i = 0
        while i < len(self):
            c = self[i]

            if c == '(':
                repeated_text, i = self._parenthesis_command_text_and_next_index(i)
                decompressed.append(repeated_text)
            else:
                decompressed.append(c)
                i += 1
        return len(''.join(decompressed))

    def _text_inside_parentheses(self, starting_parenthesis_index):
        e = self._ending_parenthesis_index(starting_parenthesis_index)
        return self[starting_parenthesis_index + 1:e]

    def _text_after_parentheses(self, starting_parenthesis_index, characters):
        e = self._ending_parenthesis_index(starting_parenthesis_index)
        return self[e + 1:e + 1 + characters]

    def _ending_parenthesis_index(self, starting_parenthesis_index):
        return self.find(')', starting_parenthesis_index)

    def _parenthesis_command_text_and_next_index(self, starting_parenthesis_index):
        text = self._text_inside_parentheses(starting_parenthesis_index)
        characters = int(text.split('x')[0])
        times = int(text.split('x')[1])
        ending_parenthesis_index = self.find(')', starting_parenthesis_index)
        return (self[ending_parenthesis_index + 1:ending_parenthesis_index + 1 + characters] * times,
                ending_parenthesis_index + characters + 1)
