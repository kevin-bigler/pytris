import numpy


class Tetromino:
    def __init__(self, matrix, name, style):
        self.matrix = matrix
    
    def rotate(self):
        pass

    def anti_rotate(self):
        pass

    def as_boolean_matrix(self):
        pass

    def as_pos_list(self):
        pass

    @property
    def style(self):
        return self._style
