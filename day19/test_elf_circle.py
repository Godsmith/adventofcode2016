from day19.elf_circle import ElfCircle, AcrossElfCircle


def test_winning_elf():
    assert ElfCircle(5).winning_elf == 3
    assert ElfCircle(6).winning_elf == 5
    assert ElfCircle(8).winning_elf == 1
    assert ElfCircle(32).winning_elf == 1


def test_across_circle_winning_elf():
    assert AcrossElfCircle(5).winning_elf == 2
    assert AcrossElfCircle(397).winning_elf == 154


# def test_indices_to_remove():
#     assert AcrossElfCircle.indices_to_remove(5, True) == {2, 4, 0}

def test_count_dead():
    assert AcrossElfCircle._count_dead([True, True, True, True], 0, 1, 4) == 0
    assert AcrossElfCircle._count_dead([False, True, True, True], 0, 1, 4) == 1
    assert AcrossElfCircle._count_dead([False, True, True, False], 3, 1, 4) == 1
    assert AcrossElfCircle._count_dead([False, True, True, False], 3, 2, 4) == 2


def test_opposite_index():
    assert AcrossElfCircle._opposite_index(0, 2, None) == 1
    assert AcrossElfCircle._opposite_index(0, 4, None) == 2
    assert AcrossElfCircle._opposite_index(3, 4, None) == 1
    assert AcrossElfCircle._opposite_index(0, 3, None) == 1
    assert AcrossElfCircle._opposite_index(0, 5, None) == 2

    # 2 is dead
    assert AcrossElfCircle._opposite_index(1, 5, [True, True, False, True, True]) == 4
    # 2 and 4 are dead
    assert AcrossElfCircle._opposite_index(3, 5, [True, True, False, True, False]) == 0
    # 2 and 4 and 0 are dead
    assert AcrossElfCircle._opposite_index(1, 5, [False, True, False, True, False]) == 3
