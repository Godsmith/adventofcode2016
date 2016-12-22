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

    @staticmethod
    def _remove_opposite(elf, elves):
        opposite_index = (elves.index(elf) + math.floor(len(elves) / 2)) % len(elves)
        return elves[:opposite_index] + elves[opposite_index + 1:]


# print(ElfCircle(3005290).winning_elf)
print(AcrossElfCircle(3005290).winning_elf)
