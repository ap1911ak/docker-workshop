import sys
import pandas as pd

print('arguments:', sys.argv)
month = sys.argv[1]


df = pd.DataFrame({"day": [1, 2], "mu,_passengers": [3, 4]})
df["month"] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet")

print(f'hello from pipeline.py, month={month}')