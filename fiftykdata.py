import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

#load table from mysql database
    # Create SQLAlchemy engine
engine = create_engine("mysql+mysqlconnector://root:Deepika%40464@localhost/educationdetails_db")

    # Load data from MySQL table
df = pd.read_sql_table('education_details', con=engine)

print(f"✅ Table loaded! Shape: {df.shape}")

# number of rows and columns
print(df.shape)
print("Done \n")
# print first 5 rows
print(df.head())
# print last 5 rows
print(df.tail())
# print data types of each column
print(df.dtypes)
# print summary statistics
print(df.describe())
# print null values in each column
print(df.isnull().sum())
# print unique values in each column
print(df.nunique())
# print number of duplicate rows
print(df.duplicated().sum())
# drop duplicate rows
df.drop_duplicates(inplace=True)
print("Duplicate rows dropped. Remaining rows:", df.shape[0])
# column names
print("Column names:")
print(df.columns.tolist())
# rename columns
df.rename(columns={
    'Student ID': 'student_id',
    'Student Name': 'student_name',
    'Age': 'age',
}, inplace=True)
print("Columns renamed:")
print(df.columns.tolist())


## Fill numeric-like columns
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['age'].fillna(df['age'].median(), inplace=True)

df['attendance_pct'] = pd.to_numeric(df['attendance_pct'], errors='coerce')
df['attendance_pct'].fillna(df['attendance_pct'].mean(), inplace=True)

# Fill categorical columns
df['gender'].fillna('Unknown', inplace=True)
df['grade'].fillna('Unknown', inplace=True)
df['course'].fillna('Unknown', inplace=True)
df['enrollment_date'].fillna('1970-01-01', inplace=True)

print(" Null values filled.")

# Compute stats
print("\n Statistics:")
print("Mean age:", df['age'].mean())
print("Median age:", df['age'].median())
print("Mode age:", df['age'].mode()[0])
print("Age Std Dev:", df['age'].std())

print("Mean attendance:", df['attendance_pct'].mean())
print("Median attendance:", df['attendance_pct'].median())
print("Mode attendance:", df['attendance_pct'].mode()[0])
print("Attendance Std Dev:", df['attendance_pct'].std())

# Save cleaned data to new table
df.to_sql(name='education_details_cleaned', con=engine, if_exists='replace', index=False)
print(" Cleaned data saved to MySQL table: education_details_cleaned")
# drop unnecessary columns
df.drop(columns=['student_id', 'student_name'], inplace=True, errors='ignore')
print(" Dropped unnecessary columns (if they existed).")
# Save cleaned data to CSV
df.to_csv('cleaned_education_data_50k.csv', index=False)
#inspect the data
print("\n Gender value counts:")
print(df['gender'].value_counts(dropna=False))

print("\n Course value counts:")
print(df['course'].value_counts(dropna=False))

print("\n Grade value counts:")
print(df['grade'].value_counts(dropna=False))

print("\n Enrollment date value counts:")
print(df['enrollment_date'].value_counts(dropna=False))

# Further clean gender
df['gender'] = df['gender'].str.strip().str.lower().replace({
    'm': 'Male',
    'male': 'Male',
    'maale': 'Male',
    'f': 'Female',
    'female': 'Female',
    'femle': 'Female',
    'other': 'Other',
    'unknown': 'Other',
    'none': 'Other',
    '': 'Other'
})

# Further clean course
df['course'] = df['course'].str.strip().str.capitalize().replace({
    'Unknown': 'Unknown',
    'None': 'Unknown'
})

# Further clean grade
df['grade'] = df['grade'].replace({
    'Unknown': 'N/A',
    'None': 'N/A',
    '': 'N/A'
})

# Further clean enrollment_date
df['enrollment_date'] = df['enrollment_date'].replace({
    '32-13-2020': '2000-01-01',
    '1970-01-01': '2000-01-01',
    'None': '2000-01-01',
    '': '2000-01-01'
})

# View final cleaned values
print("\n Final cleaned gender:\n", df['gender'].value_counts())
print("\n Final cleaned course:\n", df['course'].value_counts())
print("\n Final cleaned grade:\n", df['grade'].value_counts())
print("\n Final cleaned enrollment date:\n", df['enrollment_date'].value_counts())

# Optionally re-save to DB
df.to_sql(name='education_details_cleaned_final', con=engine, if_exists='replace', index=False)
print(" Final cleaned data saved to MySQL table: education_details_cleaned_final")
# Save final cleaned data to CSV
df.to_csv('final_cleaned_education_data_50k.csv', index=False)
# Fix age: replace negative and zero ages with median age
valid_age_median = df.loc[df['age'] > 0, 'age'].median()
df['age'] = df['age'].apply(lambda x: valid_age_median if x <= 0 else x)

# Fix attendance: replace negative attendance with mean of valid attendance
valid_attendance_mean = df.loc[df['attendance_pct'] >= 0, 'attendance_pct'].mean()
df['attendance_pct'] = df['attendance_pct'].apply(lambda x: valid_attendance_mean if x < 0 else x)

# Optionally, fix grades if 'N/A' is not acceptable (e.g., replace with mode grade)
mode_grade = df.loc[df['grade'] != 'N/A', 'grade'].mode()[0]
df['grade'] = df['grade'].replace('N/A', mode_grade)

# Optionally, fix 'Unknown' courses by replacing with most common course
mode_course = df.loc[df['course'] != 'Unknown', 'course'].mode()[0]
df['course'] = df['course'].replace('Unknown', mode_course)

print("✅ Replaced invalid numeric values and normalized categorical fields.")
# Save final cleaned data to CSV
df.to_csv('final_cleaned_education_data_50k.csv', index=False)

# Visualize cleaned data
# Compute average attendance per course
attendance_by_course = df.groupby('course')['attendance_pct'].mean().sort_values(ascending=False)

# Plot bar chart
plt.figure(figsize=(8, 5))
attendance_by_course.plot.bar(color='mediumseagreen', edgecolor='black')
plt.title('Average Attendance Percentage by Course', fontsize=14)
plt.xlabel('Course')
plt.ylabel('Average Attendance (%)')
plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.tight_layout()

# Add value labels
for index, value in enumerate(attendance_by_course):
    plt.text(index, value + 1, f'{value:.1f}%', ha='center', fontsize=10)

plt.show()

#Number of female students enrolled per course
female_counts = df[df['gender'] == 'Female']['course'].value_counts()

# Plot pie chart
plt.figure(figsize=(8, 8))
female_counts.plot.pie(autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12}, colormap='Pastel1')
plt.title('Proportion of Female Students Enrolled per Course', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.show()

#Participation levels across grades and courses
# Create pivot table for participation (number of students) by course and grade
pivot = df.pivot_table(index='course', columns='grade', aggfunc='size', fill_value=0)

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(pivot, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Participation Levels: Number of Students by Course and Grade', fontsize=14)
plt.xlabel('Grade')
plt.ylabel('Course')
plt.show()
#what is the most popular course among students
most_popular_course = df['course'].mode()[0]
print(f"The most popular course among students is: {most_popular_course}")
#clean 