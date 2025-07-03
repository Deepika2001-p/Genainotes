Estimation & Inference Concepts with Education Dataset

This document explains core statistical estimation and inference topics with code examples using a student performance dataset.

---
 1. What is Estimate?

Estimate refers to an approximate calculation or judgment of the value of a parameter based on sample data.

Example: Estimating the average math score of students from a sample of 200.

python
mean_math = df["Math_Score"].mean()


---

2. Point of Estimation

Point estimation provides a single value as an estimate of a population parameter.

Most common point estimate: Mean

python
point_estimate_math = df["Math_Score"].mean()


Other examples: median, mode

---

3. Why Do We Do Estimation?

- Studying an entire population is impractical.
- Estimation enables predictions based on samples.
- Helps in decision-making with incomplete data.

---

 4. Context for Estimation (Education Domain)

Scenario: We want to estimate the effectiveness of a test preparation course.

We calculate:
- Mean scores for students who completed the course vs. those who didn't.
- Use confidence intervals to determine reliability.

```python
completed = df[df["Test_Preparation_Course"] == "Completed"]
not_completed = df[df["Test_Preparation_Course"] == "None"]
mean_completed = completed["Math_Score"].mean()
mean_not_completed = not_completed["Math_Score"].mean()
```

---

5. Bayes' Theorem

Definition: Updates probability estimates based on new evidence.

Formula: 
P(A|B) = (P(B|A) * P(A)) / P(B)

Example: P(Completed | Reading > 80)

```python
prob_read_gt_80 = (df["Reading_Score"] > 80).mean()
prob_completed = (df["Test_Preparation_Course"] == "Completed").mean()
prob_read_gt_80_given_completed = (completed["Reading_Score"] > 80).mean()
bayes_result = (prob_read_gt_80_given_completed * prob_completed) / prob_read_gt_80
```

---

6. Inference

Inference: Drawing conclusions about a population from sample data.

Example: We infer whether completing a prep course improves writing scores.

```python
from scipy import stats
group1 = completed["Writing_Score"]
group2 = not_completed["Writing_Score"]
t_stat, p_val = stats.ttest_ind(group1, group2, alternative='greater')
```

---

 7. Density Function (KDE Plot)

Kernel Density Estimation shows the distribution of scores.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.kdeplot(df["Math_Score"], fill=True)
plt.title("Density of Math Scores")
plt.show()
```

---

 8. Normal Distribution Plot

```python
import numpy as np
from scipy.stats import norm

mean = df["Math_Score"].mean()
std = df["Math_Score"].std()
x = np.linspace(0, 100, 200)
y = norm.pdf(x, mean, std)

plt.plot(x, y, label="Normal Distribution", color="green")
plt.title("Normal Curve for Math Scores")
plt.xlabel("Score")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()
```

---

9. Confidence Margin (95% Confidence Interval)

Confidence Interval estimates a range within which the true mean lies.

```python
import scipy.stats as stats
n = len(df)
sem = stats.sem(df["Math_Score"])
margin = stats.t.ppf(0.975, n - 1) * sem
conf_interval = (mean - margin, mean + margin)
```

---

10. Hypothesis Testing

Definition: A statistical method to test assumptions (hypotheses).

Steps:
- Null hypothesis (H₀): No effect (e.g., prep course has no impact)
- Alternate hypothesis (H₁): There is an effect
- Use t-test and p-value

Example:
```python
t_stat, p_val = stats.ttest_ind(group1, group2, alternative='greater')
```

Interpretation:
- If p-value < 0.05, reject H₀ → prep course has a significant impact.

---

Summary Table

| Concept           | Description                  | Example                        |
| ----------------- | ---------------------------- | ------------------------------ |
| Estimate          | Approximate value            | Mean Math Score                |
| Point Estimation  | Single value (e.g., mean)    | `df["Math_Score"].mean()`      |
| Estimation Use    | Makes prediction from sample | Mean comparison                |
| Bayes             | Update probability           | `P(Completed \| Reading > 80)` |
| Inference         | Draw conclusion from sample  | Hypothesis test                |
| Density Plot      | Data distribution            | KDE plot                       |
| Normal Dist.      | Bell curve                   | `scipy.stats.norm`             |
| Confidence Margin | 95% range for mean           | `stats.t.ppf`                  |
| Hypothesis Test   | Verify assumptions           | t-test                         |

---

