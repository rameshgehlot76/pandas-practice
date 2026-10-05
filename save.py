import pandas as pd 

data = {
    "Name": ['John', 'Anna', 'Peter', 'Linda'],
    "Age": [28, 24, 35, 32],
    "City": ['New York', 'Paris', 'Berlin', 'London'],
    "Salary": [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)
print(df)

#df.to_csv("pandas/output.csv", index=False)
#df.to_excel("pandas/output.xlsx", index=False)
df.to_json("pandas/output.json", index=False) 



