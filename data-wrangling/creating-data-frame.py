# Load library
import pandas as pd

# Create DataFrame
dataframe = pd.DataFrame()

# Add columns
dataframe['Name'] = ['Jacky Jackson', 'Steven Stevenson']
dataframe['Age'] = [38, 25]
dataframe['Driver'] = [True, False]

# Create row
new_person = pd.Series(['Molly Mooney', 40, True], index=['Name','Age','Driver'])

# Append row
dataframe = dataframe.append(new_person, ignore_index=True)

# Show DataFrame
print(dataframe)