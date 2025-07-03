import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Connect to MySQL
engine = create_engine("mysql+mysqlconnector://root:Deepika%40464@localhost/educationdetails_db")

# Step 2: Load data from MySQL
df = pd.read_sql_table('education_details', con=engine)
print(f"✅ Loaded data from MySQL. Shape: {df.shape}")

# Step 3: Check and remove duplicate student IDs
if 'student_id' in df.columns:
    student_id_dupes = df[df.duplicated(subset='student_id', keep=False)]
    print(f"❗ Found {len(student_id_dupes)} rows with duplicate student_id values.")
    
    df.drop_duplicates(subset='student_id', keep='first', inplace=True)
    print(f"✅ Dropped duplicates based on student_id. New shape: {df.shape}")
else:
    print("⚠️ student_id column not found. Skipping duplicate check by ID.")

# Step 4: Rename columns (if needed)
df.rename(columns={
    'Student ID': 'student_id',
    'Student Name': 'student_name',
    'Age': 'age'
}, inplace=True)

# Step 5: Convert numeric columns and fill nulls
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['attendance_pct'] = pd.to_numeric(df['attendance_pct'], errors='coerce')

df['age'] = df['age'].fillna(df['age'].median())
df['attendance_pct'] = df['attendance_pct'].fillna(df['attendance_pct'].mean())

# Step 6: Fill categorical nulls
df['gender'] = df['gender'].fillna('Unknown')
df['grade'] = df['grade'].fillna('Unknown')
df['course'] = df['course'].fillna('Unknown')
df['enrollment_date'] = df['enrollment_date'].fillna('1970-01-01')

# Step 7: Fix invalid numeric values
median_age = df[df['age'] > 0]['age'].median()
df['age'] = df['age'].apply(lambda x: median_age if x <= 0 else x)

mean_attendance = df[df['attendance_pct'] >= 0]['attendance_pct'].mean()
df['attendance_pct'] = df['attendance_pct'].apply(lambda x: mean_attendance if x < 0 else x)

# Step 8: Standardize categorical values
df['gender'] = df['gender'].str.strip().str.lower().replace({
    'm': 'Male', 'male': 'Male', 'maale': 'Male',
    'f': 'Female', 'female': 'Female', 'femle': 'Female',
    'unknown': 'Other', 'none': 'Other', '': 'Other'
})

df['course'] = df['course'].str.strip().str.capitalize().replace({'Unknown': 'Unknown', 'None': 'Unknown'})
mode_course = df[df['course'] != 'Unknown']['course'].mode()[0]
df['course'] = df['course'].replace('Unknown', mode_course)

df['grade'] = df['grade'].replace({'Unknown': 'N/A', 'None': 'N/A', '': 'N/A'})
mode_grade = df[df['grade'] != 'N/A']['grade'].mode()[0]
df['grade'] = df['grade'].replace('N/A', mode_grade)

df['enrollment_date'] = df['enrollment_date'].replace({
    '32-13-2020': '2000-01-01',
    '1970-01-01': '2000-01-01',
    'None': '2000-01-01',
    '': '2000-01-01'
})

# Step 9: Save cleaned data
df.to_sql(name='education_details_cleaned_final', con=engine, if_exists='replace', index=False)
print("✅ Cleaned data saved to MySQL table: 'education_details_cleaned_final'")

df.to_csv('final_cleaned_education_data_50k.csv', index=False)
print("📁 Cleaned data also saved as 'final_cleaned_education_data_50k.csv'")

# Save final cleaned data to CSV with new name
df.to_csv('noduplicatesandnull.csv', index=False)
print("📁 Final cleaned data saved as 'noduplicatesandnull.csv'")


# plotting the graph 
# ------------------- BAR CHART: Avg Attendance by Course -------------------
plt.figure(figsize=(10, 6))
attendance_by_course = df.groupby('course')['attendance_pct'].mean().sort_values(ascending=False)
attendance_by_course.plot.bar(color='mediumseagreen', edgecolor='black')

plt.title('Average Attendance Percentage by Course', fontsize=16)
plt.xlabel('Course')
plt.ylabel('Average Attendance (%)')
plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.tight_layout()

# Add value labels
for index, value in enumerate(attendance_by_course):
    plt.text(index, value + 1, f'{value:.1f}%', ha='center', fontsize=9)

plt.savefig('attendance_by_course.png')
plt.show()

# ------------------- PIE CHART: Female Students per Course -------------------
female_counts = df[df['gender'] == 'Female']['course'].value_counts()

plt.figure(figsize=(8, 8))
female_counts.plot.pie(autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12}, colormap='Pastel1')

plt.title('Proportion of Female Students Enrolled per Course', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.savefig('female_students_pie.png')
plt.show()

# ------------------- HEATMAP: Participation by Grade and Course -------------------
pivot = df.pivot_table(index='course', columns='grade', aggfunc='size', fill_value=0)

plt.figure(figsize=(12, 6))
sns.heatmap(pivot, annot=True, fmt='d', cmap='YlGnBu')

plt.title('Participation Levels by Course and Grade', fontsize=16)
plt.xlabel('Grade')
plt.ylabel('Course')
plt.tight_layout()
plt.savefig('participation_heatmap.png')
plt.show()