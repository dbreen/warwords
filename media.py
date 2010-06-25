import os
import pygame

import conf
import constants
from utils import memoize

MEDIA_PATH = 'media'
FONT_DIR = os.path.join(MEDIA_PATH, 'fonts')
SKINS_PATH = 'skins'
PERKS_PATH = 'perks'

class MediaNotFound(Exception):
    pass

def load_image(path):
    return pygame.image.load(os.path.join(MEDIA_PATH, path))

class Media(object):
    STATIC = {
    }
    SKINNED = {
        'board': 'board.png',
        'tile': 'tile.png',
        'trough': 'trough.png',
    }
    _images = {}
    
    def __init__(self):
        pygame.font.init()
        self.letter_font = pygame.font.Font(os.path.join(FONT_DIR, constants.LETTER_FONT), constants.LETTER_SIZE)
        self.point_font = pygame.font.Font(os.path.join(FONT_DIR, constants.LETTER_FONT), constants.POINT_SIZE)
        self.widest_tile = self.letter_font.render('W', True, (0, 0, 0)).get_width() / 2
    
    def load(self):
        for key, val in self.STATIC.iteritems():
            self._images[key] = load_image(val)
        for key, val in self.SKINNED.iteritems():
            self._images[key] = load_image(os.path.join(SKINS_PATH, conf.SKIN, val))
        for file in os.listdir(os.path.join(MEDIA_PATH, SKINS_PATH, conf.SKIN, PERKS_PATH)):
            name, _, ext = file.partition('.')
            if not name: continue
            self._images['perks.%s' % name] = load_image(os.path.join(SKINS_PATH, conf.SKIN, PERKS_PATH, file))

    def __getitem__(self, key):
        try:
            return self._images[key]
        except KeyError:
            raise MediaNotFound()

    def get_tile(self, let, points):
        tile = self._images['tile'].copy()
        if let:
            letter = self.letter_font.render(let, True, constants.LETTER_COLOR)
            tile.blit(letter, (constants.LETTER_OFFSET[0] + (self.widest_tile - letter.get_width() / 2), constants.LETTER_OFFSET[1]))
        if points:
            points = self.point_font.render(str(constants.LETTER_POINTS[let]), True, constants.LETTER_COLOR)
            tile.blit(points, (constants.TILE_WIDTH - constants.POINT_OFFSET[0] - points.get_width(), constants.POINT_OFFSET[1]))
        return tile

media = Media()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = 'dan rocks'
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(constants.SCREEN)
    media.load_all()
    screen.blit(media['board'], constants.BOARD_POS)
    def draw_let(let, x, y):
        screen.blit(media[let], (
            constants.BOARD_POS[0] + constants.BOARD_BORDER + (x * (constants.BOARD_GROOVE + constants.TILE_WIDTH)),
            constants.BOARD_POS[1] + constants.BOARD_BORDER + (y * (constants.BOARD_GROOVE + constants.TILE_WIDTH))))
    def draw_word(word, x, y):
        for i, let in enumerate(word):
            if let == ' ': continue
            draw_let(let, x + i, y)
    for let in range(ord('A'), ord('Z') + 1):
        x = (let - ord('A')) % 5
        y = (let - ord('A')) / 5
        draw_let(chr(let), x, y)
    draw_let('perks.peak', 8, 2)
    draw_let('I', 9, 2)
    draw_let('perks.swap', 10, 2)
    draw_let('perks.swap', 11, 2)
    draw_word('OUT', 9, 3)
    draw_word('MY', 10, 4)
    draw_let('A', 11, 5)
    draw_let('perks.swap', 12, 5)
    draw_let('perks.swap', 13, 5)
    draw_word(word.upper(), 1, 10)
    pygame.display.flip()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

