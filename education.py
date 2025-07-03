import pandas as pd
import numpy as np
import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt


def load_and_clean_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Clean numeric fields
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['score'] = pd.to_numeric(df['score'], errors='coerce')
    df['date_enrolled'] = pd.to_datetime(df['date_enrolled'], errors='coerce')

    # Normalize string fields
    df['gender'] = df['gender'].str.strip().str.lower().replace({
        'female': 'female', 'femaLe': 'female',
        'male': 'male',
        'other': 'other'
    })

    df['course'] = df['course'].str.strip().str.lower().str.capitalize()
    df['grade'] = df['grade'].replace({'': 'N/A', None: 'N/A'})
    df['attendance'] = df['attendance'].str.strip().str.lower().replace({
        'present': 'present', 'p': 'present',
        'absent': 'absent', 'a': 'absent'
    })

    # Remove rows with critical missing data
    df = df.dropna(subset=['age', 'score', 'date_enrolled'])

    # Remove rows with negative scores
    df = df[df['score'] >= 0]

    # Final strict clean: remove any row that still has any NULL
    df = df.dropna()

    return df

def perform_statistics(df):
    print("\n✅ Statistics on cleaned data:")

    age_array = df['age'].to_numpy()
    score_array = df['score'].to_numpy()

    print(f"Mean age: {np.mean(age_array):.2f}")
    print(f"Mean score: {np.mean(score_array):.2f}")

    print(f"Median age: {np.median(age_array):.2f}")
    print(f"Median score: {np.median(score_array):.2f}")

    mode_age = pd.Series(age_array).mode()
    mode_score = pd.Series(score_array).mode()
    mode_age_val = mode_age.iloc[0] if not mode_age.empty else 'N/A'
    mode_score_val = mode_score.iloc[0] if not mode_score.empty else 'N/A'
    print(f"Mode age: {mode_age_val}")
    print(f"Mode score: {mode_score_val}")

    print(f"Standard deviation age: {np.std(age_array, ddof=1):.2f}")
    print(f"Standard deviation score: {np.std(score_array, ddof=1):.2f}")

def generate_visualizations(df):
    sns.set(style="whitegrid", palette="muted")

    # Histogram of scores
    plt.figure(figsize=(8, 5))
    sns.histplot(df['score'], bins=10, kde=True, color='skyblue')
    plt.title('Distribution of Student Scores', fontsize=14)
    plt.xlabel('Score (Marks obtained by students)', fontsize=12)
    plt.ylabel('Number of Students (Frequency)', fontsize=12)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    # Boxplot of scores by course
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='course', y='score', data=df, palette='Set2')
    plt.title('Score Distribution by Course', fontsize=14)
    plt.xlabel('Course', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Bar chart of average score by course
    plt.figure(figsize=(8, 5))
    avg_score = df.groupby('course')['score'].mean().sort_values()
    sns.barplot(x=avg_score.index, y=avg_score.values, palette='pastel')
    plt.title('Average Score per Course', fontsize=14)
    plt.xlabel('Course', fontsize=12)
    plt.ylabel('Average Score', fontsize=12)
    for i, v in enumerate(avg_score.values):
        plt.text(i, v + 1, f"{v:.1f}", ha='center', fontweight='bold')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    # Pie chart of grade distribution
    plt.figure(figsize=(6, 6))
    grade_counts = df['grade'].value_counts()
    colors = sns.color_palette('Set3')
    plt.pie(grade_counts.values, labels=grade_counts.index, autopct='%1.1f%%',
            startangle=140, colors=colors)
    plt.title('Grade Distribution among Students', fontsize=14)
    plt.tight_layout()
    plt.show()

def save_to_mysql(df):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Deepika@464",
            database="education_db"
        )
        cursor = conn.cursor()

        # Truncate table before insert
        cursor.execute("TRUNCATE TABLE students;")
        print("✅ Table truncated successfully.")

        insert_query = """
        INSERT INTO students (student_id, student_name, age, gender, course, grade, attendance, score, date_enrolled)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for _, row in df.iterrows():
            cursor.execute(insert_query, (
                int(row['student_id']),
                row['student_name'],
                int(row['age']),
                row['gender'],
                row['course'],
                row['grade'],
                row['attendance'],
                float(row['score']),
                row['date_enrolled'].date()
            ))

        conn.commit()
        print(f"✅ Inserted {df.shape[0]} fully cleaned rows into the database.")

    except mysql.connector.Error as err:
        print(f"❌ MySQL Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    file_path = "dirty_education_5000.csv"
    df = load_and_clean_data(file_path)

    print("✅ Final cleaned data preview:")
    print(df.head())

    print("\n✅ Final cleaned data info:")
    print(df.info())

    perform_statistics(df)
    generate_visualizations(df)
    save_to_mysql(df)
