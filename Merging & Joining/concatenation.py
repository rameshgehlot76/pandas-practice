# vertically (rows-wise)
# horizontally (columns-wise)

import pandas as pd 

#region1
df_Region1 = pd.DataFrame({
    'CustomerID': [1, 2],
    'CustomerName': ['John', 'Jane']
})

#region2
df_Region2 = pd.DataFrame({
    'CustomerID': [3, 4],
    'CustomerName': ['Jim', 'Jill']
})

# concatenate vertically
df_vertical = pd.concat([df_Region1, df_Region2], axis=0, ignore_index=True)
print("Vertical Concatenation:\n", df_vertical)

# concatenate horizontally
df_horizontal = pd.concat([df_Region1, df_Region2], axis=1, ignore_index=True)
print("\nHorizontal Concatenation:\n", df_horizontal)

