"""Tetris"""
import pygame
from main_loop import loop
from tetris_board import TetrisBoard

pygame.init()

board_width_squares = 5
board_height_squares = 8

screen_width = 200
screen_height = 400
bg_color = pygame.Color('grey12')

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris!')

board = TetrisBoard(board_width_squares, board_height_squares)
# screen.blit(board.surface, (0, 0))

board.occupy(1, 3)

def tick(clock):
    screen.fill(bg_color)
    board.draw(screen)


loop(tick)

