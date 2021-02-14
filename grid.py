"""Grid data structure, for convenience"""

class Grid:
    def __init__(self, width, height, initFn=lambda: {}):
        """
        Args:
            width
            height
            initFn - invoked to initialize each grid item's value. default is empty map
        """
        self.width = width
        self.height = height

        def get_row():
            return [initFn() for i in range(width)]
        self.arr = [get_row() for i in range(height)]

    def __call__(self, x, y):
        return self.arr[y][x]

    def debug_print(self):
        print('grid width x height =', len(self.arr[0]), 'x', len(self.arr))

# # g = Grid(3, 5, lambda : {'foo': 'bar'})
# g = Grid(3, 5)
# # g.debug_print()
# print('grid thing at 0, 0:', g(0,0))
# g(1, 1)['foo'] = 'babaloo'
# print('grid thing at 1, 1:', g(1,1))
# print('grid thing at 0, 0:', g(0,0))
# g(2,1)['boogie_woogie'] = 'yowza!'
# print('grid thing at 2, 1:', g(2,1))