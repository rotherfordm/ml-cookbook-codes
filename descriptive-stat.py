# Load library
import numpy as np
# Create matrix
matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])


# Return mean
print(np.mean(matrix))
#5.0

# Return variance
print(np.var(matrix))
#6.666666666666667

# Return standard deviation
print(np.std(matrix))
#2.5819888974716112

print(np.mean(matrix, axis=0))