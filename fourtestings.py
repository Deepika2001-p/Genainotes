import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Load the dataset
data = pd.read_csv("edu_study_data.csv")

# Preview first few rows
data.head()

#1.Descriptive Statistics
# Summary statistics
print(data.describe())

# Mean score by Group
print("\nMean ExamScore by Group:")
print(data.groupby("Group")["ExamScore"].mean())

# Mean score by Campaign
print("\nMean ExamScore by Campaign:")
print(data.groupby("Campaign")["ExamScore"].mean())

#2.Visualize Distributions
# Use boxplots to see differences in scores:
# By Group
sns.boxplot(x="Group", y="ExamScore", data=data)
plt.title("Exam Score Distribution by Group")
plt.show()

# By Campaign
sns.boxplot(x="Campaign", y="ExamScore", data=data)
plt.title("Exam Score Distribution by Campaign")
plt.show()

#3.parametric test (independent t-test)
#Does the average exam score differ between Group A and Group B?
# Separate scores
group_a = data[data["Group"] == "A"]["ExamScore"]
group_b = data[data["Group"] == "B"]["ExamScore"]

# t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)

print("Parametric Test - Independent t-test")
print("t-statistic =", t_stat)
print("p-value =", p_value)

#non-parametric test()
# Does the distribution of scores differ without assuming normality?
u_stat, p_value = stats.mannwhitneyu(group_a, group_b)

print("Non-Parametric Test - Mann-Whitney U")
print("U-statistic =", u_stat)
print("p-value =", p_value)

#A/B Test (Chi-Square between Campaign and Group)
# Are students in each Group recruited equally by Campaigns?
# Contingency table
contingency_campaign = pd.crosstab(data["Campaign"], data["Group"])
print(contingency_campaign)

# Chi-square test
chi2, p, dof, expected = stats.chi2_contingency(contingency_campaign)

print("\nA/B Testing - Chi-square")
print("Chi2 =", chi2)
print("p-value =", p)

#Chi-Square Test (Gender vs Group)
#Is gender associated with which Group students are in?
# Contingency table
contingency_gender = pd.crosstab(data["Gender"], data["Group"])
print(contingency_gender)

# Chi-square test
chi2, p, dof, expected = stats.chi2_contingency(contingency_gender)

print("\nChi-square Test - Gender vs Group")
print("Chi2 =", chi2)
print("p-value =", p)


