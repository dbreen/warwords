from gamemodes.base import BaseGameMode
from tiles import Tile

class StandardGameMode(BaseGameMode):
    TILES = {
        'A': (5, 1),
        'B': (4, 4),
        'C': (4, 4),
        'D': (4, 2),
        'E': (5, 1),
        'F': (4, 4),
        'G': (4, 3),
        'H': (4, 3),
        'I': (5, 1),
        'J': (1, 10),
        'K': (2, 5),
        'L': (4, 2),
        'M': (4, 4),
        'N': (4, 2),
        'O': (5, 1),
        'P': (4, 4),
        'Q': (1, 10),
        'R': (4, 1),
        'S': (5, 1),
        'T': (5, 1),
        'U': (5, 2),
        'V': (2, 5),
        'W': (4, 4),
        'X': (1, 8),
        'Y': (4, 3),
        'Z': (1, 10),
        '': (2, 0)
    }
    TILE_BANK = 7

    def get_tileset(self):
        tiles = []
        for letter, (count, points) in self.TILES.iteritems():
            for i in range(0, count):
                tiles.append(Tile(letter, points))
        return tiles
