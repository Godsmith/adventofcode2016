from day08.display import Display

with open('input.txt') as f:
    lines = f.readlines()
    display = Display(columns=50, rows=6)
    for line in lines:
        display.command(line)
    print(display.lit_pixels())
    print(str(display))
