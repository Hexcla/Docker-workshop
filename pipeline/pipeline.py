import sys 
import pandas as pd 
df = pd.DataFrame({"Day": [1, 2], "Num_passanger": [3, 4]})
month = int(sys.argv[1])
df['Month'] = month
df.to_parquet(f"data_{month}.parquet", index=False)

print(df.head())
print(f"Pipeline executed successfully! Arguments: {month}")