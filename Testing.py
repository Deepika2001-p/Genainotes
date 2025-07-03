"""
Prametric type : Parametric types refer to statistical tests or models that make assumptions about 
the parameters (like mean, variance) of the population distribution (usually a normal distribution).

parametric testing — specifically the independent t-test — to compare the average heights of women 
                     from two different states, California and Texas."""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Step 1: Simulate Population Data for Two States

# Set seed for reproducibility
np.random.seed(42)

# Group 1: Heights of women in California (mean = 64, std = 3)
california_heights = np.random.normal(loc=64, scale=3, size=10000)

# Group 2: Heights of women in Texas (mean = 65, std = 3.2)
texas_heights = np.random.normal(loc=65, scale=3.2, size=10000)

# ------------------------------
# Step 2: Take a Sample from Each Group
# ------------------------------

# Suppose we randomly sample 30 women from each group
sample_california = np.random.choice(california_heights, size=30, replace=False)
sample_texas = np.random.choice(texas_heights, size=30, replace=False)

# Calculate sample means and standard deviations
mean_cal = np.mean(sample_california)
mean_tex = np.mean(sample_texas)
std_cal = np.std(sample_california, ddof=1)
std_tex = np.std(sample_texas, ddof=1)

print("California Sample Mean:", mean_cal)
print("Texas Sample Mean:", mean_tex)
print("California Sample Std Dev:", std_cal)
print("Texas Sample Std Dev:", std_tex)

# ------------------------------
# Step 3: Perform Independent t-test
# ------------------------------

# This tests if the means of two independent groups are significantly different
t_stat, p_value = stats.ttest_ind(sample_california, sample_texas)

print("\nT-Statistic:", t_stat)
print("P-Value:", p_value)

# Interpret the result
if p_value < 0.05:
    print(" Significant difference between California and Texas women’s heights")
else:
    print(" No significant difference between the two groups")

# ------------------------------
# Step 4: Visualize the Sample Data
# ------------------------------

# Plot histograms of both samples

plt.hist(sample_california, bins=10, alpha=0.7, label='California', color='skyblue')
plt.hist(sample_texas, bins=10, alpha=0.7, label='Texas', color='orange')

# Add detailed labels and legend
plt.title("Sample Height Distributions: California vs Texas Women")
plt.xlabel("Height of women (in inches) — measured values from samples of 30 women each")
plt.ylabel("Number of women in each height range (Frequency)")
plt.legend()
plt.show()
