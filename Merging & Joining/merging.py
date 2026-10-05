#pd.merge(df1, df2, on="Column_Name", how="type of join") 

import pandas as pd 

# Customer DataFrame
customer_data = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5],
    'CustomerName': ['John', 'Jane', 'Jim', 'Jill', 'Jack'],
})

# Order DataFrame
order_data = pd.DataFrame({
    'CustomerID': [1, 2, 3, 6, 7],
    'OrderAmount': [100, 200, 300, 400, 500]
})


# Merge the two DataFrames on 'CustomerID'

df_merged = pd.merge(customer_data, order_data, on='CustomerID', how='inner')
print('Inner Join:\n', df_merged)

