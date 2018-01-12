# STEP 1: LOAD DATA “train.csv” WHILE ASSIGNING -1 AS NULL VALUES

import pandas as pd

train=pd.read_csv('/Users/sanket/Downloads/train.csv',na_values=-1)
df_train = pd.DataFrame(train)

# STEP 5: UNDERSAMPLING - EXPORT BALANCED DATA TO A CSV FILE
import csv
import pandas as pd
import numpy as np

df_filtered_1 = df_train.query('target==1')
df_filtered_0 = df_train.query('target==0')

rows_1 = df_filtered_1
rows_1_len = len(rows_1.index)
rows_0 = df_filtered_0.sample(rows_1_len)

print(len(rows_1))
print(len(rows_0))

rows_0_1 = rows_0.append(rows_1, ignore_index=True)
print(len(rows_0_1))

rows_0_1.to_csv('/Users/sanket/Downloads/train_u.csv',mode='w', index=False)