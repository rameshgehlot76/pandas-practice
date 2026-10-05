import pandas as pd

data = {
    "Name": ['John', 'Anna', 'Peter', 'Linda', 'James', 'Emily', 'Michael', 'Sarah', 'David', 'Olivia'],
    "Age": [28, 24, 35, 32, 29, 31, 27, 30, 33, 26],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 85000, 90000, 95000],
    "Performance Score": [85, 90, 78, 92, 88, 84, 91, 89, 87, 93]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary'] > 70000] 
print('Employees with salary > 70000')
print(high_salary) 


# Display rows based on multiple conditions 
multiple_conditions = df[(df['Salary'] > 50000) & (df['Age'] > 30)]
print('\nEmployees with salary > 50000 and age > 30')
print(multiple_conditions)


#using OR condition
or_condition = df[(df['Age'] > 35) | (df['Performance Score'] > 90)] 
print('\nEmployees with age > 35 or performance score > 90') 
print(or_condition)

 
