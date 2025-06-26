import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load dataset
df = pd.read_csv("student_performance_dataset.csv")
print(df.head())

# ===== POINT ESTIMATION =====
# Mean (Point Estimate)
mean_math = df["Math_Score"].mean()
print("Mean Math Score:", mean_math)

mean_reading = df["Reading_Score"].mean()
print("Mean Reading Score:", mean_reading)

mean_writing = df["Writing_Score"].mean()
print("Mean Writing Score:", mean_writing)

# Median
median_math = df["Math_Score"].median()
print("Median Math Score:", median_math)

median_reading = df["Reading_Score"].median()
print("Median Reading Score:", median_reading)

# ===== BAYES INFERENCE =====
# P(Completed | Reading > 80)
prob_read_gt_80 = (df["Reading_Score"] > 80).mean()
prob_completed = (df["Test_Preparation_Course"] == "Completed").mean()
prob_read_gt_80_given_completed = (
    df[df["Test_Preparation_Course"] == "Completed"]["Reading_Score"] > 80).mean()

bayes_result = (prob_read_gt_80_given_completed * prob_completed) / prob_read_gt_80
print("P(Completed | Reading > 80):", bayes_result)

# ===== CONDITIONAL PROBABILITIES =====
# P(Math > 70 | Reading > 80)
prob_math_gt_70_given_read_gt_80 = (
    df[(df["Reading_Score"] > 80) & (df["Math_Score"] > 70)].shape[0] /
    df[df["Reading_Score"] > 80].shape[0]
)
print("P(Math > 70 | Reading > 80):", prob_math_gt_70_given_read_gt_80)

# P(Writing > 75 | Reading > 80)
prob_writing_gt_75_given_read_gt_80 = (
    df[(df["Reading_Score"] > 80) & (df["Writing_Score"] > 75)].shape[0] /
    df[df["Reading_Score"] > 80].shape[0]
)
print("P(Writing > 75 | Reading > 80):", prob_writing_gt_75_given_read_gt_80)

# ===== DENSITY FUNCTION PLOT =====
sns.kdeplot(df["Math_Score"], fill=True)  # fixed 'shade' to 'fill'
plt.title("Density Plot of Math Scores")
plt.xlabel("Score")
plt.ylabel("Density")
plt.grid(True)
plt.show()

# ===== CONFIDENCE INTERVAL (95%) =====
n = len(df)
sem = stats.sem(df["Math_Score"])  # standard error
margin = stats.t.ppf(0.975, n - 1) * sem  # 95% confidence margin
conf_interval = (mean_math - margin, mean_math + margin)  # fixed variable
print("95% Confidence Interval:", conf_interval)

# ===== HYPOTHESIS TESTING =====
group1 = df[df["Test_Preparation_Course"] == "Completed"]["Writing_Score"]
group2 = df[df["Test_Preparation_Course"] == "None"]["Writing_Score"]

t_stat, p_val = stats.ttest_ind(group1, group2, alternative='greater')
print("T-statistic:", t_stat)
print("P-value:", p_val)
