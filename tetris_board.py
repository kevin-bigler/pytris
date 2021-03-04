"""Keeps track of the space where pieces are placed, etc"""
import pygame

from grid import Grid

light_grey = (200, 200, 200)

square_width = 30
square_height = 30
square_color = light_grey
square_border_width = 3

class TetrisBoard:
    def __init__(self, width, height):
        self._grid = Grid(width, height, Square)
        
        self.surface = pygame.Surface((width * square_width, height * square_height))

        for sq, (x, y) in self.grid:
            sq.rect.left = x * square_width
            sq.rect.top = y * square_height

        # self.draw(self.surface)

    @property
    def grid(self):
        return self._grid

    def __call__(self, x, y):
        return self.grid(x, y)

    def __iter__(self):
        return self.grid.__iter__

    def occupied(self, x, y):
        return self.grid(x, y).occupied is True

    def draw(self, screen):
        screen.blit(self.surface, (0, 0))
        self.surface.fill(square_color)
        for sq, (x, y) in self.grid:
            sq.draw(self.surface)

    def occupy(self, x, y):
        self.grid(x, y).occupied = True

class Square():
    def __init__(self):
        self.occupied = False
        self.position = (0, 0)

    def __repr__(self):
        return 'X' if self.occupied is True else 'O'

    def draw(self, surface):
        fill_color = pygame.Color('black') if sq.occupied else square_color
        pygame.draw.rect(self.surface, pygame.Color('black'), sq.rect, square_border_width)
        
        self.surface.fill(fill_color)
        surface.blit(self.surface)
    
# b = TetrisBoard(10, 15)
# b.grid(9, 14).occupied = True
# print(b.grid.width, b.grid.height)
# for (val, (x, y)) in b.grid:
#     print(type(val), x, y)
#     print(val)
#     print('is ', x, y, 'occupied?', b.occupied(x, y))