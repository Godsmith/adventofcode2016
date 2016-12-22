class Scrambler:
    @staticmethod
    def do(operation, input_):
        operation_list = operation.split(' ')
        if 'rotate left' in operation:
            return Scrambler._rotate_left(int(operation_list[2]), input_)
        if 'rotate right' in operation:
            return Scrambler._rotate_right(int(operation_list[2]), input_)
        if 'rotate based' in operation:
            return Scrambler._rotate_based_on_position(operation_list[6], input_)
        if 'swap position' in operation:
            return Scrambler._swap_position(int(operation_list[2]), int(operation_list[5]), input_)
        if 'swap letter' in operation:
            return Scrambler._swap_letter(operation_list[2], operation_list[5], input_)
        if 'reverse' in operation:
            return Scrambler._reverse(int(operation_list[2]), int(operation_list[4]), input_)
        if 'move' in operation:
            return Scrambler._move(int(operation_list[2]), int(operation_list[5]), input_)
        else:
            raise ValueError('Invalid operation: "%s"' % operation)

    @staticmethod
    def do_all(operations, input_):
        for operation in operations:
            input_ = Scrambler.do(operation, input_)
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
    def _rotate_based_on_position(letter, s: str):
        index = s.index(letter)
        steps = 1 if index >= 4 else 0
        return Scrambler._rotate_right(steps + 1 + index, s)

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
        string_without_source_letter = s[:source] + s[source+1:]
        return string_without_source_letter[:target] + s[source] + string_without_source_letter[target:]
