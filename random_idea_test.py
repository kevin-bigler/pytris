def sum(*args):
    total = 0
    for x in args:
        total += x
    return total

def combine(a, b):
    return a + b

print('sum 1,2', sum(1,2))
print('sum *(1,2)', sum(*(1,2)))
print('combine 1,2', combine(1,2))
print('combine *(1,2)', combine(*(1,2)))