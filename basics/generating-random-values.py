# Load library
import numpy as np

# Set seed
np.random.seed(1)

# Generate three random floats between 0.0 and 1.0
rand_float = np.random.random(3)
print(rand_float)

# Generate three random integers between 1 and 10
rand_integers = np.random.randint(0, 11, 3)
print(rand_integers)

# Draw three numbers from a normal distribution with mean 0.0
rand_norm_dist = np.random.normal(0.0, 1.0, 3)
print(rand_norm_dist)

# Draw three numbers from a logistics distribution with mean 0.0 and scale of 1.0
rand_logistics_dist = np.random.logistic(0.0, 1.0, 3)
print(rand_logistics_dist)

# Draw three numbers greater than or equal to 1.0 and less than 2.0
rand_uniform = np.random.uniform(1.0, 2.0, 3)
print(rand_uniform)