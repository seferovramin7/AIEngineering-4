# what_we_will_achieve.py
# GOAL: To quickly analyze student data, find the average score for each subject,
# and identify the top-performing student in 'Math'.

import pandas as pd
import numpy as np

# In this lesson, you will learn to work with data like this.
# This is a dictionary, a standard Python data structure.
data = {
    'StudentID': ['S01', 'S02', 'S03', 'S04', 'S05', 'S06'],
    'Name': ['Ali', 'Vali', 'Sara', 'Kamran', 'Leyla', 'Samir'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Score': [85, 92, 78, 88, 95, np.nan],  # np.nan represents missing data
    'StudyHours': [10, 12, 8, 11, 15, 9]
}

# You will learn to create a DataFrame - a powerful, table-like structure.
df = pd.DataFrame(data)

print("----------- Original Student Data -----------")
print(df)
print("\n")

# You'll learn how to handle problems, like missing scores.
# We'll fill the missing score with the average of other scores.
average_score = df['Score'].mean()
df['Score'].fillna(average_score, inplace=True)

print("----------- Data After Cleaning (No Missing Scores) -----------")
print(df)
print("\n")

# You'll be able to ask complex questions and get answers easily.
# Q1: What is the average score for each subject?
print("----------- Average Score Per Subject -----------")
avg_score_by_subject = df.groupby('Subject')['Score'].mean().round(2)
print(avg_score_by_subject)
print("\n")

# Q2: Who is the top-performing student in Math?
print("----------- Top Student in Math -----------")
math_students = df[df['Subject'] == 'Math']
top_math_student = math_students.loc[math_students['Score'].idxmax()]
print(top_math_student)
print("\n")

print("🎉 By the end of this lesson, you will be able to perform this entire analysis yourself!")
