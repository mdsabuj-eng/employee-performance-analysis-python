# Employee Performance Analysis Project (Python + SQLite + Pandas)

# 🔹 Step 1: Import Required Libraries
import sqlite3
import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Visualization Settings
sns.set(style="whitegrid")
plt.style.use('seaborn-v0_8-darkgrid')

# 🔹 Step 2: Download SQLite Database from GitHub
url = 'https://github.com/mdsabuj-eng/employee-performance-analysis-python/raw/refs/heads/main/employee_analysis.db'
db_path = 'employee_analysis.db'

urllib.request.urlretrieve(url, db_path)
print("Database downloaded successfully!")

# 🔹 Step 3: Connect to SQLite Database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
print("Connected to the SQLite database!")

# 🔹 Step 4: Check Available Tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables available in the database:", tables)

# 🔹 Step 5: Preview First 5 Rows from Employee Table
query = "SELECT * FROM Employee LIMIT 5;"
df_sample = pd.read_sql_query(query, conn)
print("\nSample Data from Employee Table:")
print(df_sample)

# 🔹 Step 6: Load Full Table into Pandas DataFrame
df_full = pd.read_sql_query("SELECT * FROM Employee;", conn)

# 🔹 Step 7: Data Overview
print("\n--- DataFrame Info ---")
df_full.info()

print("\n--- Descriptive Statistics ---")
print(df_full.describe())

# 🔹 Step 8: Check for Missing Values
print("\nMissing Values per Column:")
print(df_full.isnull().sum())

# 🔹 Step 9: Simple KPIs Calculation
avg_salary = df_full['Salary'].mean()
max_perf = df_full['PerformanceScore'].max()
min_perf = df_full['PerformanceScore'].min()
total_employees = df_full.shape[0]

print("\n--- KPI Summary ---")
print(f"Total Employees: {total_employees}")
print(f"Average Salary: {avg_salary:.2f}")
print(f"Highest Performance Score: {max_perf}")
print(f"Lowest Performance Score: {min_perf}")

# 🔹 Step 10: Visualization 1 - Gender Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Gender', data=df_full, palette='Set2')
plt.title('Gender Distribution of Employees')
plt.show()

# 🔹 Step 11: Visualization 2 - Department Wise Employee Count
plt.figure(figsize=(8,5))
sns.countplot(x='Department', data=df_full, palette='viridis')
plt.title('Employee Count by Department')
plt.xticks(rotation=45)
plt.show()

# 🔹 Step 12: Visualization 3 - Salary Distribution
plt.figure(figsize=(6,4))
sns.histplot(df_full['Salary'], kde=True, color='coral')
plt.title('Salary Distribution')
plt.show()

# 🔹 Step 13: Close SQLite Connection
conn.close()
print("\nSQLite connection closed.")
