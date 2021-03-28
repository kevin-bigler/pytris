"""Keeps track of the space where pieces are placed, etc"""
import pygame

from grid import Grid


class TetrisBoard:
    def __init__(self, width, height, square_width, square_height):
        self._grid = Grid(width, height, Square)
        
        self.surface = pygame.Surface((width * square_width, height * square_height))

        for sq, (x, y) in self.grid:
            sq.rect.left = x * square_width
            sq.rect.top = y * square_height

    @property
    def grid(self):
        return self._grid

    def __call__(self, x, y):
        return self.grid(x, y)

    def __iter__(self):
        return self.grid.__iter__

    def occupied(self, x, y):
        return self.grid(x, y).occupied is True

    def occupy(self, x, y):
        self.grid(x, y).occupied = True

class Square():
    def __init__(self, x=0, y=0):
        self._occupied = False
        self.position = (x, y)

    @property
    def occupied(self):
        return self._occupied is True

    def occupy(self):
        self._occupied = True

    def __repr__(self):
        return 'X' if self.occupied else 'O'
    
    @property
    def color(self):
        return pygame.Color('green') if sq.occupied else square_color
