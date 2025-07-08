Python Revision (NumPy, Pandas, scikit-learn, Matplotlib)
| Library          | What it does                              | Example                         |
| ---------------- | ----------------------------------------- | ------------------------------- |
|   NumPy          | Handles numerical data & arrays           | Create arrays for ML datasets   |
|   Pandas         | Handles data in tabular form (DataFrames) | Load CSV files, clean data      |
|   Matplotlib     | For visualizing data (charts, graphs)     | Plot a line graph               |
|   scikit-learn   | Used for ML algorithms and preprocessing  | Build a linear regression model |

Machine learning : it is a type of artificial intelligence where machines learn from data and make predictions (or) decisions without being explicitely programmed.
Example: Predicting house prices based on area and number of rooms.
         Gmail automatically classifying emails into spam and inbox.

Machine learning usecases
| Domain           | Use-Case Example                            |
| ---------------- | ------------------------------------------- |
|   Healthcare     | Predict disease based on patient data       |
|   Finance        | Fraud detection in credit card transactions |
|   Retail         | Recommend products to customers (Amazon)    |
|   Education      | Predict if a student is at risk of failing  |
|   Self-driving   | Cars recognizing pedestrians and road signs |

Machine learning process flow
1.Define the problem
E.g., Predict student performance.

2.Collect Data
E.g., Students’ test scores, attendance, study hours.

3.Clean & Prepare Data
Handle missing values, normalize scores.

4.Choose a Model

Examples of Models:
Linear Regression: To predict continuous values (like house prices).
Decision Trees: For classification tasks (pass/fail prediction).
Clustering: For grouping similar data (unsupervised learning).

5.Train the Model: Feed the cleaned data to the ML algorithm so it can learn patterns and relationships.
Example:
Give the model data on study hours and test scores → Let it learn how these relate to passing or failing.
Give the model house features → Let it learn how these affect price.

6.Test & Evaluate
See how well the model predicts unseen data.

7.Deploy & Monitor: Use the model in real-world apps.
Example:
Student Performance: Deploy a model in a school system that predicts which students need extra help.
House Prices: Deploy a model on a real estate website to suggest prices for new house listings.

machine learning categories
| Category             | What It Means                                | Example                                  |
| -------------------- | -------------------------------------------- | ---------------------------------------- |
|   Supervised ML      | Train with labeled data                      | Predict house price from size & location |
|   Unsupervised ML    | No labels; find patterns                     | Group customers by buying behavior       |
|   Reinforcement ML   | Learn by trial & error (rewards & penalties) | Teaching a robot to walk                 |

Linear regression : It is a machine learning algorithm used to predict a continuous value based on input value.
                    Fits a straight line (y = mx + c) to data points.
Finds the best slope (m) and intercept (c) to minimize prediction error.
Example: Predict student score based on study hours.

Gradient Descent : it is an optimization algorithm used to find the best parameters (like slope and intercept in linear regression) by minimizing the error.
Example:
In linear regression, gradient descent adjusts the slope and intercept to fit the best line.