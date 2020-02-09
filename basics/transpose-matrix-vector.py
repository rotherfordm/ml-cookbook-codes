# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])

# Transpose matrix
print(matrix.T)

'''
Transposing is a common operation in linear algebra where the column and row
indices of each element are swapped. One nuanced point that is typically overlooked
outside of a linear algebra class is that, technically, a vector cannot be transposed
because it is just a collection of values:
'''

# Transpose vector
print(np.array([1, 2, 3, 4, 5, 6]).T)


'''
However, it is common to refer to transposing a vector as converting a row vector to
a column vector (notice the second pair of brackets) or vice versa:
'''
# Tranpose row vector
print(np.array([[1, 2, 3, 4, 5, 6]]).T)