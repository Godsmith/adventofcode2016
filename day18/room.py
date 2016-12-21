class Room:
    @staticmethod
    def make_tile(tiles):
        if ('^^' in tiles and '.' in tiles) or ('..' in tiles and '^' in tiles):
            return '^'
        else:
            return '.'

    @staticmethod
    def make_row(row):
        extended_row = '.' + row + '.'
        output = []
        for i in range(1, len(row) + 1):
            tile_input = extended_row[i - 1:i + 2]
            output.append(Room.make_tile(tile_input))
        return ''.join(output)

    @staticmethod
    def make_rows(row, n):
        output = [row]
        while len(output) < n:
            output.append(Room.make_row(output[-1]))
        return output

    @staticmethod
    def count_safe_tiles(rows):
        return sum(s.count('.') for s in rows)


print(Room.count_safe_tiles(Room.make_rows(
    '.^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....', 400000)))
