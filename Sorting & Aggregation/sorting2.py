import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [25, 30, 22],
    "Salary": [50000, 60000, 45000] 
}

df = pd.DataFrame(data)

df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print('Sorted Age by Descending Order')
print(df) 