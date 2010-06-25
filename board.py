import constants
from media import media


class Board(object):
    def __init__(self):
        self.width, self.height = constants.BOARD_SIZE
        self.tiles = [None for i in range(0, self.width * self.height)]
    
    def get_tile(self, x, y):
        return self.tiles[x + y * self.width]
    
    def set_tile(self, tile, x, y):
        self.tiles[x + y * self.width] = tile
        
    def render(self, screen):
        screen.blit(media['board'], constants.BOARD_POS)
        for i in range(0, self.width * self.height):
            if self.tiles[i]:
                self.render_tile(screen, self.tiles[i], i % self.width, i / self.width)
    
    def render_tile(self, screen, tile, x, y):
        screen.blit(tile.image, (
            constants.BOARD_POS[0] + constants.BOARD_BORDER + (x * (constants.BOARD_GROOVE + constants.TILE_WIDTH)),
            constants.BOARD_POS[1] + constants.BOARD_BORDER + (y * (constants.BOARD_GROOVE + constants.TILE_WIDTH))
        ))
