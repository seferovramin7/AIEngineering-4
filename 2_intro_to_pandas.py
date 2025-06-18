# 2_intro_to_pandas.py
# TOPIC: Organizing and exploring data with Pandas.

import pandas as pd

print("----------- Part 1: Pandas Series and DataFrames -----------")
# A Series is like a single column of data.
# A DataFrame is a table, made up of multiple Series. It's the most used object in Pandas.

# You can create a DataFrame from a Python dictionary.
data = {
    'Name': ['Ali', 'Vali', 'Sara'],
    'Age': [22, 23, 21],
    'City': ['Baku', 'Ganja', 'Sumgait']
}
df_from_dict = pd.DataFrame(data)
print("DataFrame created from a dictionary:")
print(df_from_dict)


print("\n----------- Part 2: Loading Data from a File -----------")
# This is the most common way to get data into Pandas.
# We'll load the 'sample_student_data.csv' file.
# Make sure the CSV file is in the same folder as this Python script.
# If you are running this in an environment like Google Colab,
# you would first need to upload the file.
try:
    df = pd.read_csv('sample_student_data.csv')
except FileNotFoundError:
    print("\n---")
    print("Error: 'sample_student_data.csv' not found.")
    print("Please make sure the CSV file is in the same directory as the script.")
    print("---")
    exit()


print("\n----------- Part 3: Inspecting the Data -----------")
# Let's look at our loaded data without printing the whole thing.
print("First 5 rows of the data (head):")
print(df.head(2))

print("\nLast 3 rows of the data (tail):")
print(df.tail(3))

print("\nGet a concise summary of the DataFrame (info):")
# .info() is very useful to see data types and non-missing values.
df.info()

print("\nGet a quick statistical summary (describe):")
# .describe() gives you count, mean, std, min, max etc. for numerical columns.
print(df.describe())


print("\n----------- Part 4: Selecting Data -----------")
# Selecting a single column (returns a Pandas Series)
subjects = df['Subject']
print("The 'Subject' column:")
print(subjects.head())

# Selecting multiple columns (returns a new DataFrame)
name_and_score = df[['Name', 'Score']]
print("\nThe 'Name' and 'Score' columns:")
print(name_and_score.head())

# Selecting rows with .iloc (integer location)
print("\nThe third row of data (index 2):")
print(df.iloc[2])

# Selecting rows and columns with .loc (label based)
# Get the 'Score' for the student with StudentID 'S003'
# First, we set StudentID as the index to make selection easier
df_indexed = df.set_index('StudentID')
print("\nScore for student S003:")
# FIX: Corrected 'S03' to 'S003' to match the data format.
print(df_indexed.loc['S063', 'Score'])


print("\n----------- Part 5: Data Cleaning -----------")
# Real-world data is often messy. Let's find missing values.
print("Check for missing values in each column:")
print(df.isnull().sum())
# FIX: Corrected comment to reflect the actual number of missing values (5).
# From the .info() and .isnull().sum() output,
# we see the 'Score' column has 5 missing values.

# Option 1: Drop rows with any missing values.
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values (notice the reduced count):")
print(df_dropped.info())


# Option 2: Fill missing values. This is often better.
# Let's fill the missing score with 0.
df_filled = df.fillna(value={'Score': 0})
print("\nDataFrame after filling missing score with 0:")
# We'll check the specific rows where the score was previously NaN.
# First, find out which indexes had null values.
null_score_indexes = df[df['Score'].isnull()].index
print(df_filled.loc[null_score_indexes])


print("\n----------- Part 6: Changing Data Types -----------")
# The 'Score' column was loaded as a float because of the missing value (NaN).
# Let's convert our filled DataFrame's Score column to an integer.
df_filled['Score'] = df_filled['Score'].astype(int)
print("\nInfo after changing Score to integer:")
df_filled.info()
print("\nFirst 5 rows of the final, cleaned DataFrame:")
print(df_filled.head())