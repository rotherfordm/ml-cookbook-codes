# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, -1, 3], [1, 1, 6], [3, 8, 9]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# View eigenvalues
print(eigenvalues)
# array([ 13.55075847,
# 0.74003145,
# -3.29078992])

# View eigenvectors
print(eigenvectors)
# array([[-0.17622017, -0.96677403, -0.53373322],
# [-0.435951 , 0.2053623 , -0.64324848],
# [-0.88254925, 0.15223105, 0.54896288]])
