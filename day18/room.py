class Room:
    @staticmethod
    def make_tile(tiles):
        if ('^^' in tiles and '.' in tiles) or ('..' in tiles and '^' in tiles):
            return '^'
        else:
            return '.'
