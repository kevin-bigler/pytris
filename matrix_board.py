from pygame.math import Vector2
from grid import Grid
import numpy

class MatrixBoard:
    """Tetris Matrix, ie playing area where tetrominoes appear"""
    def __init__(self, width = 10, height = 20):
        """Width and height values are by default set to the Tetris standard: 10 squares wide x 20 squares high"""
        pass

    def as_binary_matrix(self):
        """Matrix of the entire board as binary values, 1 indicating occupied and 0 indicating open spaces.
        returns numpy.ndarray"""
        pass

    def as_pos_list(self):
        """List of occupied positions in the board.
        returns Vector2[]"""
        pass

    def as_style_matrix(self):
        """Matrix of the entire board in terms of each square's style value (color/pattern/whatever).
        returns numpy.ndarray"""
        pass