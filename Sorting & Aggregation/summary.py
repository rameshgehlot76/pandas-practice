# This module contains functions for sorting and aggregating data.

"""
df["Column Name"].mean()
df["Column Name"].sum()
df["Column Name"].min()
df["Column Name"].max()
"""

import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [25, 30, 22],
    "Salary": [10000, 20000, 30000] 
}

df = pd.DataFrame(data)

avg_salary = df['Salary'].mean()
print(avg_salary)

