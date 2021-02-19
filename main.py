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

light_grey = (200, 200, 200)
square = pygame.Rect((0, 0), (10, 10))

def tick(screen):
    print('tick')
    square.left += 1
    square.top += 2
    pygame.draw.rect(screen, light_grey, square)

loop(tick)

