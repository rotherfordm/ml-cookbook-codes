# Load library
import pandas as pd

# Create URL
url = 'https://tinyurl.com//titanic-csv'

# Load data
dataframe = pd.read_csv(url)

# Select first row
print(dataframe.iloc[0])

# Select three rows
print(dataframe.iloc[1:4])

# Select three rows
print(dataframe.iloc[:4])

# Set index
dataframe = dataframe.set_index(dataframe['Name'])

print(dataframe)

# Show row
print(dataframe.loc['Allen, Miss Elisabeth Walton'])