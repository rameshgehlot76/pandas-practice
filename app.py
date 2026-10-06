import pandas as pd 

#read data from a CSV, JSON, Excel file into a dataframe

#df = pd.read_json("pandas/sample_Data.json", encoding="utf-8")
df = pd.read_excel("pandas/SampleSuperstore.xlsx")   
print(df) 

#encoding="latin-1" or "utf-8" is used to read data from a CSV file which contains special characters.  
#gcsfs library help you to read data from a cloud 

