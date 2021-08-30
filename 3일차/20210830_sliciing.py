import numpy as np
vector = [1, 2, 3, 4, 5]
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]
)
print(matrix[:2, 3:], matrix[:2, 3:].shape)


print(matrix[4], matrix[4].shape)
print(matrix[4, :], matrix[4, :].shape)
print(matrix[4:, :], matrix[4:, :].shape)

print(matrix[:, :2], matrix[:, :2].shape)

print(matrix[1, :2], matrix[1, :2].shape)
print(matrix[1:2, :2], matrix[1:2, :2].shape)



