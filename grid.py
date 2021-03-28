"""Grid data structure, for convenience"""

class Grid:
    def __init__(self, width, height, initFn=lambda: {}):
        """
        Args:
            width
            height
            initFn - invoked to initialize each grid item's value, ie initFn(x, y). default is empty map
        """
        self.width = width
        self.height = height

        def get_row(y):
            return [initFn(x, y) for x in range(width)]
        self.arr = [get_row(y) for y in range(height)]

    def __call__(self, x, y):
        return self.arr[y][x]

    def debug_print(self):
        print('grid width x height =', len(self.arr[0]), 'x', len(self.arr))

    def __iter__(self):
        """Each element is returned as a tuple of (val, pos), as in (val, (x, y))"""
        for y in range(self.height):
            for x in range(self.width):
                yield (self.arr[y][x], (x, y))

    def vals(self):
        """Iterator for grid values"""
        for y in range(self.height):
            for x in range(self.width):
                yield self.arr[y][x]

# # g = Grid(3, 5, lambda : {'foo': 'bar'})
# g = Grid(3, 5)
# # g.debug_print()
# print('grid thing at 0, 0:', g(0,0))
# g(1, 1)['foo'] = 'babaloo'
# print('grid thing at 1, 1:', g(1,1))
# print('grid thing at 0, 0:', g(0,0))
# g(2,1)['boogie_woogie'] = 'yowza!'
# print('grid thing at 2, 1:', g(2,1))