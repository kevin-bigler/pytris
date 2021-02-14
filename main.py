def say_hello(name='fred'):
    print('hello', name)

def say_bye(name, suffix):
    print('bye', name, suffix or '...')

say_hello()
say_hello('joe')
say_hello(name='bob')

say_bye('bob', 'jr')
# say_bye(suffix='senior', 'bob')
say_bye(suffix='II', name='bob')
say_bye('bobo', suffix='VI')