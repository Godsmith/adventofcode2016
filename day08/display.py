class Display:
    def __init__(self, rows, columns):
        self.array = [['.'] * columns for _ in range(rows)]

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.array])

    def rect(self, width, height):
        for row in range(height):
            for column in range(width):
                self.array[row][column] = '#'

    def rotate_column(self, x, steps):
        column = self._get_column(x)
        rotated_column = self._rotate_array(column, steps)
        self._set_column(x, rotated_column)

    def rotate_row(self, y, steps):
        row = self._get_row(y)
        rotated_row = self._rotate_array(row, steps)
        self._set_row(y, rotated_row)

    def command(self, s):
        if 'rect' in s:
            width = int(s.split(' ')[1].split('x')[0])
            height = int(s.split(' ')[1].split('x')[1])
            self.rect(width, height)
        elif 'row' in s:
            y = int(s.split('=')[1].split(' ')[0])
            steps = int(s.split(' by ')[1].split(' ')[0])
            self.rotate_row(y, steps)
        elif 'column' in s:
            x = int(s.split('=')[1].split(' ')[0])
            steps = int(s.split(' by ')[1].split(' ')[0])
            self.rotate_column(x, steps)

    def lit_pixels(self):
        return sum([row.count('#') for row in self.array])

    def _set_column(self, x, new_column):
        for row in range(len(self.array)):
            self.array[row][x] = new_column[row]

    def _set_row(self, y, new_row):
        self.array[y] = new_row

    def _get_column(self, x):
        return [self.array[i][x] for i in range(len(self.array))]

    def _get_row(self, y):
        return self.array[y]

    @staticmethod
    def _rotate_array(array, steps):
        effective_steps = steps % len(array)
        return array[-effective_steps:] + array[:-effective_steps]
