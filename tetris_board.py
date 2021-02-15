"""Keeps track of the space where pieces are placed, etc"""
from grid import Grid

class TetrisBoard:
    def __init__(self, width, height):
        self.grid = Grid(width, height)