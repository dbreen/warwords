import os
import pygame
import random
import time

MEDIA = "."

SCREEN = (900, 700)
FRAMERATE = 30

BOARD_OFFSET = (30, 30)
BOARD_BORDER = 10
GAME_WIDTH = 15
TILE_WIDTH = 34
GROOVE_WIDTH = 5

clock = None
font = None
screen = None
board = None
tile = None

last_move = 0
position = (0, 0)

class Img(object):
    def __init__(self, img):
        self.image = pygame.image.load(os.path.join(MEDIA, img)).convert()
        self.rect = self.image.get_rect()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self, coords):
        self.rect.left = coords[0]
        self.rect.top = coords[1]

def gameloop():
    global last_move, position
    clock.tick(FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.exit()
    if time.time() - last_move > 3:
        last_move = time.time()
        position = (random.randint(0, GAME_WIDTH-1), random.randint(0, GAME_WIDTH - 1))
        movetile(screen, tile, position)
    screen.fill((0,0,0))
    board.draw(screen)
    tile.draw(screen)
    pos = font.render('Tile Pos: %s' % str(position), 1, (0, 250, 0))
    screen.blit(pos, (650, 200))
    pygame.display.flip()

def movetile(screen, tile, pos):
    tile.move((
        (BOARD_OFFSET[0] + BOARD_BORDER + (pos[0] * (TILE_WIDTH + GROOVE_WIDTH))),
        (BOARD_OFFSET[1] + BOARD_BORDER + (pos[1] * (TILE_WIDTH + GROOVE_WIDTH)))
    ))

if __name__ == "__main__":
    pygame.init()
    font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode(SCREEN)
    
    board = Img('board1.png')
    tile = Img('tile1.png')
    board.move(BOARD_OFFSET)
    clock = pygame.time.Clock()
    
    while True:
       gameloop()
