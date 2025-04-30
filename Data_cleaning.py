import pandas as pd
data = pd.read_csv(r"C:\Users\USER\Downloads\healthcare_messy_data.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(data.head())

#replace forty with 40
data["Age"] = data['Age'].replace('forty', 40)
print(data.head(10))

#   # coercing error to NAN
data['Age'] = pd.to_numeric(data['Age'], errors = 'coerce')
print(data.head(30))

#replace with mean value. 
data['Age'].fillna(data['Age'].mean())
pd.set_option('display.max_column', None)
print(data.head(30))