# 3_practical_application.py
# TOPIC: Combining NumPy and Pandas to analyze data.

import pandas as pd
import numpy as np # We still need NumPy for its functions

# --- Step 1: Load the Data ---
# Load the dataset we used in the previous lesson.
df = pd.read_csv('sample_student_data.csv')
print("----------- Original Data -----------")
print(df)
print("\n")


# --- Step 2: Clean the Data ---
# We have a missing 'Score'. A good strategy is to fill it with the mean score.
# This is better than filling with 0 because it doesn't skew the average.

# First, calculate the mean of the *existing* scores.
mean_score = df['Score'].mean()
print(f"The average score of the class is: {mean_score:.2f}")

# Now, fill the missing value (NaN) with this mean.
df['Score'].fillna(mean_score, inplace=True) # inplace=True modifies the DataFrame directly
print("\n----------- Data After Cleaning -----------")
print(df)
print("\n")


# --- Step 3: Analyze with GroupBy ---
# This is one of the most powerful features of Pandas.
# We want to find the average score for each subject.

# Group the DataFrame by the 'Subject' column, then select the 'Score' column,
# and finally, calculate the mean for each group.
avg_by_subject = df.groupby('Subject')['Score'].mean()

print("----------- Average Score by Subject -----------")
print(avg_by_subject)
print("\n")

# We can do more complex aggregations too!
# Let's find the average score AND average study hours per subject.
agg_results = df.groupby('Subject').agg({
    'Score': 'mean',
    'StudyHours': 'mean'
})
print("----------- Aggregated Results by Subject -----------")
print(agg_results.round(2)) # .round(2) makes it look cleaner
print("\n")


# --- Step 4: Answering a Specific Question ---
# Question: Which subject has the highest average study hours?

# We can sort our aggregated results to find out.
sorted_by_study = agg_results.sort_values(by='StudyHours', ascending=False)

print("----------- Subjects Sorted by Average Study Hours -----------")
print(sorted_by_study)
print(f"\nAnswer: '{sorted_by_study.index[0]}' has the highest average study hours.")

print("\nCongratulations! You have successfully loaded, cleaned, and analyzed a dataset.")