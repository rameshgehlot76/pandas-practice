import pandas as pd

data = {
    "Name": ['John', 'Anna', 'Peter', 'Linda', 'James', 'Emily', 'Michael', 'Sarah', 'David', 'Olivia'],
    "Age": [28, 24, 35, 32, 29, 31, 27, 30, 33, 26],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 85000, 90000, 95000],
    "Performance Score": [85, 90, 78, 92, 88, 84, 91, 89, 87, 93]
}

df = pd.DataFrame(data)

#display the dataframe 
print("Sample Dataframe")
print(df)


#Display single column 
print("Names (Single column returns series)") 
name = df["Name"] 
print(name) 


#Display multiple columns
subset = df[["Name", "Salary"]]
print('\nSubset with Name and Salary')  
print(subset)


