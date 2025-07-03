import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Data
exam_scores = np.array([55, 60, 65, 70, 75, 80, 85]).reshape(-1, 1)
admission = np.array([0, 0, 0, 1, 1, 1, 1])

# Create logistic regression model
model = LogisticRegression()
model.fit(exam_scores, admission)

# Predict for a new student with score 68
new_score = 68
predicted_prob = model.predict_proba([[new_score]])
predicted_class = model.predict([[new_score]])

print(f"Probability of admission for score {new_score}: {predicted_prob[0][1]:.2f}")
print(f"Predicted class (0=No Admission, 1=Admitted): {predicted_class[0]}")

# Plot
score_range = np.linspace(50, 90, 100).reshape(-1, 1)
prob_admit = model.predict_proba(score_range)[:, 1]

plt.scatter(exam_scores, admission, color='blue', label='Actual Data')
plt.plot(score_range, prob_admit, color='red', label='Probability of Admission')
plt.xlabel("Entrance Exam Score")
plt.ylabel("Probability of Admission")
plt.title("Logistic Regression: Exam Score vs Admission Chance")
plt.legend()
plt.grid(True)
plt.show()
