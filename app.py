import pandas as pd
import numpy as np

# Creating a pandas Series from a list
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Creating a DataFrame from a dictionary
data = {
            "calories": [420, 380, 390],
                "duration": [50, 40, 45]
                }
df = pd.DataFrame(data)
print(df)

# Accessing rows by label using loc
print(df.loc[0])       # Returns row at index 0 as a Series
print(df.loc[[0, 1]])  # Returns rows at index 0 and 1 as a DataFrame

# Creating a DataFrame from a list of lists with custom index and columns
df2 = pd.DataFrame(
            [[4, 7, 10],
                  [5, 8, 11],
                  [6, 9, 12]],
                index=[1, 2, 3],
                    columns=['a', 'b', 'c']
                    )
print(df2)

