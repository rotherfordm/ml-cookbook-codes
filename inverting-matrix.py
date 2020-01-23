# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, 4],
[2, 5]])

# Calculate inverse of matrix
print(np.linalg.inv(matrix))
# array([[-1.66666667, 1.33333333],
# [ 0.66666667, -0.33333333]])