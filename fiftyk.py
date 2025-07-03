import pandas as pd
import numpy as np
import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt

# load csv file
df= pd.read_csv('dirty_education_data_50k.csv')
# connect to mysql database
db = mysql.connector.connect(
    host="localhost",
    user="root",    
    password="Deepika@464",
    database="education_db"
)
# number of rows and columns
print(df.shape)
print("Done \n")
# print first 5 rows
print(df.head())
# print last 5 rows
print(df.tail())
# print data types of each column
print(df.dtypes)
# print summary statistics
print(df.describe())
# print null values in each column
print(df.isnull().sum())
# print unique values in each column
print(df.nunique())
# print number of duplicate rows
print(df.duplicated().sum())
# drop duplicate rows
df.drop_duplicates(inplace=True)
print("Duplicate rows dropped. Remaining rows:", df.shape[0])
# column names
print("Column names:")
print(df.columns.tolist())
# rename columns
df.rename(columns={
    'Student ID': 'student_id',
    'Student Name': 'student_name',
    'Age': 'age',
}, inplace=True)
print("Columns renamed:")