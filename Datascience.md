What is Data Science: Data Science is the study of data to find useful patterns and insights using math, statistics, and programming.

steps involved in datascience : 

1.collecting the data(SQL, APIs, Scrapers)
2.cleaning the data( Pandas, Numpy)
3.analyzing the data
4.Building models(Scikit-learn, TensorFlow)
5.virtualizing the results(Matplotlib, Tableau)

Example: An online store

Tracks customer clicks (collect)
Removes duplicate data (clean)
Finds best-selling products (analyze)
Predicts future demand (model).

Business Intelligence : predicts past data.(uses reports and dashboards)
example: Monthly sales report
Data science: looks at past + predicts future (uses ML and AI )
Example: Predicting next month’s sales.

Tools :
Programming: Python, R
Data Handling: SQL, Excel
Visualization: Tableau, PowerBI, Matplotlib
Big Data Tools: Hadoop, Spark
ML/AI Frameworks: TensorFlow, Scikit-learn

steps for Data cleaning : It means fixing or removing wrong, incomplete, duplicate, or irrelevant data so your analysis is accurate.

steps : 
1.Remove Duplicates: df.drop_duplicates(inplace=True)
2.Handle Missing Values (Nulls): remove full row if too many nulls.
                                 fill with mean,median,mode
                                 use a default value.
df['age'].fillna(df['age'].mean(), inplace=True)
df.dropna(inplace=True)  # Removes rows with nulls

3.Fix Wrong Data Types : df['date'] = pd.to_datetime(df['date'])
                         df['marks'] = pd.to_numeric(df['marks'])

4.Standardize Column Names: 

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

5.Remove Outliers: outliers are values that are too high or too low compared to the rest of the data.
Example: In a school dataset:
Most teachers’ salaries = $40,000–$60,000
But there’s 1 entry: $1,000,000 (maybe entered by mistake).this is an outlier because it doesn’t make sense in this context.
2 methods in outliers:1.Interquartile Range (IQR)
Step 1: Find Q1 and Q3
Q1 (25th percentile) = value below which 25% of data falls.
Q3 (75th percentile) = value below which 75% of data falls.
ex dataset : 35K, 40K, 45K, 50K, 55K, 60K, 1,000,000
Q1:40K Q3:60K  so IQR = Q3-Q1 = 20k. 
then filterout outliers
                   Q1 = df['salary'].quantile(0.25)
                   Q3 = df['salary'].quantile(0.75)
                   IQR = Q3 - Q1
                   df = df[(df['salary'] >= Q1 - 1.5 * IQR) & (df['salary'] <= Q3 + 1.5 * IQR)]
method 2 : Z-Score (Standard Score)
A Z-score (also called a standard score) tells you how far a value is from the mean of your data in terms of standard deviations.
They help us standardize data and detect values that are too far from the center of the distribution.
Z > 3 or Z < -3 = very rare, treat as outlier.
If Z = 0 → The value is exactly at the mean.
If Z = +1 → The value is 1 standard deviation above the mean.
If Z = -1 → The value is 1 standard deviation below the mean.



6.Correct Typos or Inconsistent Values:  Fix spelling mistakes or unify formats.
df['gender'] = df['gender'].replace({'M': 'Male', 'F': 'Female', 'male': 'Male'})
Example: "Male", "male", "M" → standardize to "Male"

7.Filter Irrelevant Data: Remove rows or columns not needed for your analysis.
                          df = df.drop(columns=['student_id'])


8.Convert Categorical to Numeric (if needed): df['gender'] = df['gender'].map({'Male': 0, 'Female': 1})

9.Normalize or Scale the Data: Needed when values have very different ranges.
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[['math_score']] = scaler.fit_transform(df[['math_score']])

10.Audit Final Data: Final check: Are all values valid. Check value ranges, data types, nulls again.


Life cycle of the datascience :

1️⃣ Problem Understanding: Understand the problem you are solving and define clear goals.

Example: A school wants to predict which students might fail so they can offer extra help.

2️⃣ Data Collection: Gather data from various sources like databases, APIs, web scraping, or sensors.

Example: Collect students’ grades, attendance, and participation data.

3️⃣ Data Cleaning: Fix missing, incorrect, or inconsistent data.

Example: Fill missing attendance records, remove duplicate rows.

4️⃣ Data Exploration (EDA): Analyze data with charts and statistics to find patterns.

Example: Plot scores vs. attendance to see if low attendance leads to poor grades.

5️⃣ Feature Engineering: Create new useful columns (features) from existing data.

Example: Create a new feature: average test score from all subject scores.

6️⃣ Model Building: Train Machine Learning models to make predictions.

Example: Use a decision tree to predict student performance.

7️⃣ Model Evaluation: Test how accurate the model is using metrics (accuracy, precision, recall).

Example: Check if the model predicts failing students correctly.

8️⃣ Deployment: Put the model into a real system (app, website, or school management system).

Example: School staff get an alert if a student is at risk of failing.

9️⃣ Monitoring and Maintenance: Watch the system for errors and update the model if data changes.

Example: Retrain the model every year with new student data.



