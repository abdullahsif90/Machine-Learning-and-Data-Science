import numpy as np
import pandas as pd

# File Paths
input_file = "pakistani_employee_data_practice.csv"
output_file = "pakistani_employee_data_cleaned.csv"

# 1.Load Dataset
df = pd.read_csv(input_file)

# 2. Convert Numeric Columns (Vectorized)
numeric_cols = [
    "Emp_ID",
    "Age",
    "Salary_PKR",
    "Experience_Years",
    "Performance_Rating",
]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

# 3. Clean Duplicates & Invalid Values
df.drop_duplicates(inplace=True)
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Replace negative salaries with NaN
df.loc[df["Salary_PKR"] < 0, "Salary_PKR"] = np.nan

# 4. Impute Missing Values with Median
fill_cols = ["Age", "Salary_PKR", "Performance_Rating"]
df[fill_cols] = df[fill_cols].fillna(df[fill_cols].median())

# 5. Remove Salary Outliers (3 Standard Deviations)
mean_sal = df["Salary_PKR"].mean()
std_sal = df["Salary_PKR"].std()

lower_bound = mean_sal - (3 * std_sal)
upper_bound = mean_sal + (3 * std_sal)

df = df[(df["Salary_PKR"] >= lower_bound) & (df["Salary_PKR"] <= upper_bound)]

# 6. Save Cleaned Dataset
df.to_csv(output_file, index=False)

print("Data Cleaning Completed Successfully!")