# Topic
# 1- how big is your dataset?
# 2- what are the names of columns? 

# shape and columns 

import pandas as pd 

data = {
    "Name": ['John', 'Anna', 'Peter', 'Linda', 'James', 'Emily', 'Michael', 'Sarah', 'David', 'Olivia'],
    "Age": [28, 24, 35, 32, 29, 31, 27, 30, 33, 26],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 85000, 90000, 95000],
    "Performance Score": [85, 90, 78, 92, 88, 84, 91, 89, 87, 93]
}

df = pd.DataFrame(data) 
print(df)
print(f'Shape: {df.shape}')
print(f'Column Names: {df.columns}')

# (10, 4)
# (10000, 20)

