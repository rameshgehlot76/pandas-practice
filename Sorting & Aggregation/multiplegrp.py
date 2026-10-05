import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun', 'Ravi', 'Sita'],
    "Age": [25, 30, 22, 28, 24],
    "Salary": [50000, 60000, 45000, 55000, 48000] 
}

df = pd.DataFrame(data)

grouped = df.groupby(["Age","Name"]) ["Salary"].sum()
print(grouped)

