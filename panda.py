import pandas as pd
# read/import the file
df = pd.read_csv('vgsales.csv')

# to get shape of table in file
df.shape 

# Generate descriptive statistics
df.describe()

# Return a Numpy Representation of the Dataframe.
df.values
