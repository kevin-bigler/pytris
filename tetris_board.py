"""Keeps track of the space where pieces are placed, etc"""
import pygame

from grid import Grid

class TetrisBoard:
    def __init__(self, width, height):
        self._grid = Grid(width, height, Square)

    @property
    def grid(self):
        return self._grid

    def occupied(self, x, y):
        return self.grid(x, y).occupied is True

square_width = 10
square_height = 10
class Square():
    def __init__(self):
        self.occupied = False,
        self.rect = pygame.Rect((0, 0), (square_width, square_height))

    def __repr__(self):
        return 'X' if self.occupied is True else 'O'
    
b = TetrisBoard(10, 15)
b.grid(9, 14).occupied = True
print(b.grid.width, b.grid.height)
for (val, (x, y)) in b.grid:
    print(type(val), x, y)
    print(val)
    print('is ', x, y, 'occupied?', b.occupied(x, y))