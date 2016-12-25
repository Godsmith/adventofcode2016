class Scrambler:
    @staticmethod
    def do(operation, input_, reverse=False):
        operation_list = operation.split(' ')
        if 'rotate left' in operation:
            direction = 1 if not reverse else -1
            return Scrambler._rotate_left(direction * int(operation_list[2]), input_)
        if 'rotate right' in operation:
            direction = 1 if not reverse else -1
            return Scrambler._rotate_right(direction * int(operation_list[2]), input_)
        if 'rotate based' in operation:
            return Scrambler._rotate_based_on_position(operation_list[6], input_, reverse)
        if 'swap position' in operation:
            return Scrambler._swap_position(int(operation_list[2]), int(operation_list[5]), input_)
        if 'swap letter' in operation:
            return Scrambler._swap_letter(operation_list[2], operation_list[5], input_)
        if 'reverse' in operation:
            return Scrambler._reverse(int(operation_list[2]), int(operation_list[4]), input_)
        if 'move' in operation:
            a = int(operation_list[2])
            b = int(operation_list[5])
            if reverse:
                a, b = b, a
            return Scrambler._move(a, b, input_)
        else:
            raise ValueError('Invalid operation: "%s"' % operation)

    @staticmethod
    def do_all(operations, input_, reverse=False):
        if reverse:
            operations = reversed(operations)
        for operation in operations:
            input_ = Scrambler.do(operation, input_, reverse)
        return input_

    @staticmethod
    def _rotate_right(steps, s):
        length = len(s)
        return s[-steps % length:] + s[:-steps % length]

    @staticmethod
    def _rotate_left(steps, s):
        length = len(s)
        return s[steps % length:] + s[:steps % length]

    @staticmethod
    def _rotate_based_on_position(letter, s: str, reverse):
        if not reverse:
            index = s.index(letter)
            steps = 1 if index >= 4 else 0
            return Scrambler._rotate_right(steps + 1 + index, s)
        else:
            string_to_try = s
            i = 0
            while True:
                string_after_rotation = Scrambler._rotate_based_on_position(letter, string_to_try, False)
                if string_after_rotation == s:
                    return string_to_try
                i += 1
                string_to_try = Scrambler._rotate_left(i, s)

    @staticmethod
    def _swap_position(p1, p2, s: str):
        list_ = list(s)
        c1 = list_[p1]
        list_[p1] = list_[p2]
        list_[p2] = c1
        return ''.join(list_)

    @staticmethod
    def _swap_letter(c1, c2, s: str):
        list_ = list(s)
        p1 = s.index(c1)
        p2 = s.index(c2)
        list_[p1] = c2
        list_[p2] = c1
        return ''.join(list_)

    @staticmethod
    def _reverse(p1, p2, s):
        return s[:p1] + ''.join(reversed(s[p1:p2 + 1])) + s[p2 + 1:]

    @staticmethod
    def _move(source, target, s):
        string_without_source_letter = s[:source] + s[source + 1:]
        return string_without_source_letter[:target] + s[source] + string_without_source_letter[target:]
