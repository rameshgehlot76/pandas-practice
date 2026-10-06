#adding columns

import pandas as pd

data = {
    "Name": ['John', 'Anant', 'Peter', 'Lalita', 'James', 'Emily', 'Michael', 'Sarah', 'David', 'Olivia'],
    "Age": [28, 36, 35, 39, 29, 31, 27, 30, 33, 26],
    "Salary": [50000, 80000, 70000, 70000, 55000, 65000, 75000, 85000, 90000, 95000],
    "Performance Score": [85, 90, 78, 82, 88, 84, 91, 89, 87, 93]
}

df = pd.DataFrame(data)
print(df)

df["Bonus"] = df["Salary"] * 0.1
print(df)


#using insert()
# df.insert(location, "Column_Name", some_data) 
df.insert(0, "Employee ID", [10,20,30,40,50,60,70,80,90,100])
print(df)
