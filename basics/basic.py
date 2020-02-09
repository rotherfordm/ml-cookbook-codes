import numpy as np
from scipy import sparse

#create a vector as row
vector_row = np.array([1, 2, 3])

#create a vector as column
vector_column = np.array([[1], [2], [3]])

#create matrix
matrix = np.array([[1, 2], [1, 2], [1, 2]])


matrix_object = np.mat([[1, 2], [1, 2], [1, 2]])

matrix_sparse = sparse.csr_matrix(matrix)

# print(vector_row)
# print(vector_column)
# print(matrix)
# print(matrix_object)

# print(matrix_sparse)

matrix_large = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)

matrix_large_sparce = sparse.csr_matrix(matrix_large)

# print(matrix_sparse)
# print('')
# print(matrix_large_sparce)

vector = np.array([1, 2, 3, 4, 5, 6])

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(vector[2])
# print(matrix[2, 0])
# print(vector[:])
# print(vector[:3])
# print(vector[3:])
# print(vector[-1])
# print(matrix[:2, :])
# print(matrix[:, 1:2])
# print(matrix[:, 1:2])


matrix = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])

# print(matrix.shape)
# print(matrix.size)
# print(matrix.ndim)


matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])

add_100 = lambda i : i + 100

vectorized_add_100 = np.vectorize(add_100)

print(vectorized_add_100(matrix))