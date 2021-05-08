import numpy as np


# print('array:', np.array([0, 1, 2]))
# print(type(np.array([0, 1, 2])))
# print(np.zeros((10, 20)))

starting_matrix_str = """
0,1,0
1,1,1
0,0,0
"""

# filter out empty lines
matrix = [line.strip().split(',') for line in starting_matrix_str.splitlines() if len(line) > 0 and not str.isspace(line)]
print(matrix)


matrix2 = np.array([[0, 1, 0], [1, 1, 1], [0, 0, 0]])
matrix3 = np.array(matrix, int)
print(matrix2)
print(matrix3)
# print(matrix)
# print('rotate')
# print(np.rot90(matrix))
# print('rotate')
# print(np.rot90(matrix, 2))
# print('anti rotate')
# print(np.rot90(matrix, -1))