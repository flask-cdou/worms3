import pandas as pd
df= pd.read_table('./data.txt', sep='|', header=3).dropna(axis=1)
for id in df['城市ID']:
    print('id:',id)


