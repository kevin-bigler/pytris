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
from tetris_board import TetrisBoard


# board widith and height in # squares
board_width = 5
board_height = 8
board = TetrisBoard(board_width, board_height)
screen.blit(board.surface, (0, 0))
# print(board)

def tick(screen):
    # print('tick')
    # board.draw(screen)
    pygame.display.update()
            



loop(tick)

