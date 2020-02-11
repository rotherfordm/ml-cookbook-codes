# Load scikit-learn's datasets
from sklearn import datasets

# Load digits dataset
digits = datasets.load_digits()
# boston_data = datasets.load_boston()
# iris_data = datasets.load_iris()


# Create features matrix
features = digits.data

# Create target vector
target = digits.target

# View first observation
print(features[0])
