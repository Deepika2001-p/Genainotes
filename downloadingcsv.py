import numpy as np
import pandas as pd

np.random.seed(42)

# Number of students
n_students = 1500

# Create DataFrame
data = pd.DataFrame({
    "StudentID": range(1, n_students + 1),
    "Gender": np.random.choice(["Male", "Female"], size=n_students),
    "Group": np.random.choice(["A", "B"], size=n_students),
    "Campaign": np.random.choice(["Email", "Social Media"], size=n_students)
})

# Assign Exam Scores
data.loc[data["Group"] == "A", "ExamScore"] = np.random.normal(70, 10, size=(data["Group"] == "A").sum())
data.loc[data["Group"] == "B", "ExamScore"] = np.random.normal(75, 12, size=(data["Group"] == "B").sum())

# Round
data["ExamScore"] = data["ExamScore"].round(2)

# Save to CSV
data.to_csv("edu_study_data.csv", index=False)

print("✅ Dataset saved as 'edu_study_data.csv' in your current folder.")

