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



board_width = 5
board_height = 8
board = Grid(board_width, board_height, initFn=square)
for i in range(board_width):
    for j in range(board_height):
        sq = board(i, j)
        sq['rect'].left = i * square_width
        sq['rect'].top = j * square_height
        sq['x'] = i
        sq['y'] = j


def tick(screen):
    # print('tick')
    for i in range(board_width):
        for j in range(board_height):
            pygame.draw.rect(screen, light_grey, squareRect)



loop(tick)

