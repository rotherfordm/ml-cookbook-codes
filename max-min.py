# Load library
import numpy as np
# Create matrix
matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
# Return maximum element
print(np.max(matrix))

# Return minimum element
print(np.min(matrix))

print(np.max(matrix, axis=0))

print(np.max(matrix, axis=1))