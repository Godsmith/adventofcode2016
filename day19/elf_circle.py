import math


class ElfCircle:
    def __init__(self, n):
        self._n = n

    @property
    def winning_elf(self):
        elves = list(range(1, self._n + 1))
        last_one_was_odd = False
        starting_position = 0
        while len(elves) > 1:
            last_elf = elves[-1]
            elves = elves[starting_position::2]
            if last_elf == elves[-1]:
                starting_position = 1
            else:
                starting_position = 0
        return elves[0]


class AcrossElfCircle(ElfCircle):
    @property
    def winning_elf(self):
        elves = list(range(1, self._n + 1))
        while len(elves) > 1:
            remaining_elf_numbers = list(elves)
            for elf in remaining_elf_numbers:
                print(elf)
                if elf in elves:
                    elves = self._remove_opposite(elf, elves)
        return elves[0]

    @property
    def winning_elf2(self):
        elves = list(range(1, self._n + 1))
        elf_count = self._n
        while elf_count > 1:
            print(elf_count)
            opposite_index = (math.floor(elf_count / 2))
            elves = elves[:opposite_index] + elves[opposite_index + 1:]
            elves = elves[1:] + [elves[0]]
            elf_count -= 1
        return elves[0]

    # @staticmethod
    # def indices_to_remove(elf_count, first_elf_gets_to_act):
    #     acting_elf_index = 0
    #     removed_indices = []
    #     offsets = [0] * elf_count
    #     while acting_elf_index < elf_count:
    #         opposite_index = (acting_elf_index + math.floor(elf_count) / 2) % elf_count

    # @staticmethod
    # def _offsets_from_living_list(self, living_list):
    #     pass
    #
    # @staticmethod
    # def _opposite_index(index, count, is_living=None):
    #     if is_living is None:
    #         is_living = [True] * count
    #     opposite_index_before_offset = (index + math.floor(count / 2)) % count
    #     dead_up_to_current_index = is_living[:opposite_index_before_offset + 1].count(False)
    #     last_index = opposite_index_before_offset
    #     current_index = opposite_index_before_offset + dead_up_to_current_index
    #     while True:
    #         change_in_offset_since_last_index = AcrossElfCircle._count_dead(is_living, last_index, current_index, count)
    #         if change_in_offset_since_last_index == 0:
    #             return current_index % count
    #         else:
    #             last_index = current_index
    #             current_index += change_in_offset_since_last_index

    @staticmethod
    def _count_dead(is_living, starting_index, offset, count):
        return [is_living[i % count] for i in range(starting_index, starting_index + offset)].count(False)



    @staticmethod
    def _remove_opposite(elf, elves):
        opposite_index = (elves.index(elf) + math.floor(len(elves) / 2)) % len(elves)
        return elves[:opposite_index] + elves[opposite_index + 1:]


