# Need to install module before you can use this
import pandas as pd

# pandas uses *dataframes*. These are like tables.
# a dataframe holds a set of data-entries. Data is organized into *columns*, where each column holds a list of data points

# You can make a new dataframe from a dictionary,
# where each key is a column name that maps to its values
d = { "name" : [ "Ellie", "Gayatri", "Rebecca", "Rishab" ],
      "year" : [ "Junior", "Junior", "Senior", "Junior" ],
      "major" : [ "Psychology", "CS", "CS", "MechE" ]
    }

df = pd.DataFrame(d)
print(df)

# You can also make a new dataframe by loading a pre-existing CSV
icecream_df = pd.read_csv("icecream.csv")
print(icecream_df)
print(icecream_df.head())

# Once you've created a dataframe, you can access the columns directly using indexing with the column name
print(df["name"])
print(df["major"])

# You can also add a new column, by setting the index to a new list. The list must be the same length as the existing data.

df["ice cream"] = [ "peach", "chocolate", "caramel", "rocky road" ]
print(df)

# If you want to access an individual piece of data, you need to iterate over the dataframe,
# accessing each row one at a time.

# iterrows iterates over both the numerical indexes and the row lists of the dataframe. It's like for-range and for-each combined.
for index, row in df.iterrows():
    print(index)
    print(row)
    # Then you can index into the row based on column names.
    print("Name:", row["name"])
    print()