import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Data
hours = np.array([2, 4, 6, 8, 10]).reshape(-1, 1)  # input (X)
marks = np.array([50, 65, 75, 85, 95])           # output (y)

# Step 2: Create the model
model = LinearRegression()

# Step 3: Train the model
model.fit(hours, marks)

# Step 4: Predict marks for a new student
new_hours = 7
predicted_marks = model.predict([[new_hours]])
print(f"Predicted marks for {new_hours} study hours: {predicted_marks[0]:.2f}")

# Step 5: Plot
plt.scatter(hours, marks, color='blue', label='Actual Marks')
plt.plot(hours, model.predict(hours), color='red', label='Regression Line')
plt.scatter(new_hours, predicted_marks, color='green', s=100, label='Predicted')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Marks")
plt.title("Linear Regression: Study Hours vs Exam Marks")
plt.legend()
plt.grid(True)
plt.show()
