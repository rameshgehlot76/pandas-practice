import pandas as pd

data = {
    "Name": ['John',None, 'Peter', 'Linda', 'James', 'Emily', 'Michael', 'Sarah', 'David', 'Olivia'],
    "Age": [28, None, 35, 32, 29, 31, 27, 30, 33, 26],
    "Salary": [50000, None, 70000, 80000, 55000, 65000, 75000, 85000, 90000, 95000],
    "Performance Score": [85, None, 78, 92, 88, 84, 91, 89, 87, 93]
}

df = pd.DataFrame(data)
print(df)

# axis = 0 means it drop all empty rows
# axis = 1 means it drop all empty columns 

# df.dropna(axis = 0,inplace=True)
df.dropna(inplace=True) 
print(df)

