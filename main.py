"""Tetris"""

# draw GUI
# - layout
#   - board
#     - grid of squares
#   - hud
#     - score, time, level
#     - next piece(s) indicator

# track state
# - board
# - level, time, score
# - current piece (shape, location)
# - next pieces

# timing
# - loop
# - interval for "gravity" effect

import pygame
from main_loop import loop
from grid import Grid

light_grey = (200, 200, 200)
squareRect = pygame.Rect((0, 0), (10, 10))


def square():
    return {
        'occupied': False,
        'rect': pygame.Rect((0, 0), (10, 10))
    }

width = 5
height = 8
board = Grid(5, 8, initFn=square)
# board.debug_print()
for i in range(width):
    for j in range(height):
        board(i, j)['rect'] # TODO create the rect at the right coords


def tick(screen):
    pass
    # print('tick')
    # pygame.draw.rect(screen, light_grey, squareRect)



loop(tick)

