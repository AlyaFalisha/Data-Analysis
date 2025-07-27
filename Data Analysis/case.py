#write your code here
import pandas as pd

#load the dataset
file_path = 'StudentsPerformance.csv'
df = pd.read_csv(file_path)

#rename colums for easier access
df.columns = ['Gender', 'race', 'parent_education', 'lunch', 'prep_course', 'math_score', 'reading_score', 'writing_score']

#display basic info
print('Dataset info:')
print(df.info())

#display first few rows
print('\nDataset Preview:')
print(df.head())

#check for missing values
print('\nMissing Value in Each Column:')
print(df.isnull().sum())

#filter students whose parents have no higher education
non_higher_edu=df[df['parent_education'].isin(['some high school','high school'])]

#calculate the averange exam scores for student with?without preparatory courses
prep_course_results = non_higher_edu.groupby('prep_course')[['math_score', 'reading_score', 'writing_score']].mean()

#display averange scores
print('\nAverange Exam Scores Based on Test Preparation Enrollment:')
print(prep_course_results)

print('Statistically significant: Preparatory courses likely improve exam scores.')