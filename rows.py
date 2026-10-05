# head()  tail() 
# methods are used to return the first n rows and last n rows of a DataFrame respectively. 
# By default, both methods return 5 rows.
# You can specify the number of rows to return by passing an integer as an argument to these methods.

import pandas as pd
df = pd.read_json("pandas/output.json")

print('Display 10 rows of first')
print(df.head(10))

print('Display 10 rows of last')
print(df.tail(10))

