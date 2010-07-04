import random

from media import media

class TileHolder(object):
    def __init__(self, tiles=[]):
        self.tiles = tiles

    def remaining(self):
        return len(self.tiles)
    
    def insert(self, tile):
        self.tiles.append(tile)
    

class TileBag(TileHolder):
    def draw(self):
        return self.tiles.pop(random.randint(0, len(self.tiles) - 1))
    

class TileTrough(TileHolder):
    def render(self, screen):
        screen.blit(media['trough'], constants.TROUGH_POS)
        for pos, tile in enumerate(self.tiles):
            self.render_tile(screen, tile, pos)

    def render_tile(self, screen, tile, pos):
        screen.blit(tile.image, (
            constants.TROUGH_POS[0] + constants.TROUGH_BORDER + (pos * (constants.TROUGH_GROOVE + constants.TILE_WIDTH)),
            constants.TROUGH_POS[1] + constants.TROUGH_BORDER
        ))

class Tile(object):
    LETTER = 1
    BLANK = 2
    
    def __init__(self, letter=None, points=0):
        self.tile_type = self.LETTER if letter else self.BLANK
        self.letter = letter if letter else ''
        self.points = points
        self.image = media.get_tile(self.letter, points)


if __name__ == "__main__":
    import constants, gamemodes, pygame
    from board import Board

    pygame.init()
    screen = pygame.display.set_mode(constants.SCREEN)
    media.load()

    gamemode = gamemodes.get_game_mode('standard')
    board = Board()
    trough = TileTrough()
    tileset = gamemode.get_tileset()
    tilebag = TileBag(tileset)
    
    # draw random tiles
    for row in range(0, 5):
        for i in range(0, gamemode.TILE_BANK):
            tile = tilebag.draw()
            board.set_tile(tile, i, row)
    
    # draw player tiles
    for i in range(0, gamemode.TILE_BANK):
        trough.insert(tilebag.draw())

    trough.render(screen)
    board.render(screen)

    pygame.display.flip()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
