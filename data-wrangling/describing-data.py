# Load library
import pandas as pd

# Create URL
url = 'https://tinyurl.com/titanic-csv'

# Load data
dataframe = pd.read_csv(url)

# Show two rows
print(dataframe.head(2))

# Show dimensions
print(dataframe.shape)

# Show dimensions
print(dataframe.describe())