from grid import Grid

def test_iter_with_pos():
    foo = Grid(3, 5)

    for val in foo:
        print('foo val:', val)

    print('')

    for val in foo:
        d, pos = val
        print('val split:', d, pos)

    for val in foo:
        d, (x, y) = val
        d['x'] = x
        d['y'] = y

    for val in foo:
        print('foo val at end:', val)

def test_iter():
    foo = Grid(6, 10)

    for val in foo.vals():
        print('val:', val)

    for d, (x, y) in foo:
        d['x'] = f'x is {x}'
        d['y'] = f'y is {y}'

    for val in foo.vals():
        print('val at end:', val)


def test_iter_other_syntax():
    foo = Grid(3, 5)

    for val in foo:
        print('val:', val)

test_iter_other_syntax()