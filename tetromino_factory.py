from tetromino import Tetromino


def create_tetromino(name):
    # TODO: impl cases
    match name.upper():
        case 'O':
        case 'T':
        case 'I':
        case 'L':
        case 'J':
        case 'S':
        case 'Z':
        case '_':
            raise Exception(f'Unrecognized tetromino name: {name}')