from day19.elf_circle import ElfCircle, AcrossElfCircle


def test_winning_elf():
    assert ElfCircle(5).winning_elf == 3
    assert ElfCircle(6).winning_elf == 5
    assert ElfCircle(8).winning_elf == 1
    assert ElfCircle(32).winning_elf == 1


def test_across_circle_winning_elf():
    assert AcrossElfCircle(5).winning_elf == 2
