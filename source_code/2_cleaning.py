# STEP 2: LOAD DATA “train_u.csv” WHILE ASSIGNING -1 AS NULL VALUES

import pandas as pd
train = pd.read_csv('/Users/sanket/Downloads/train_u.csv',na_values=-1)

# STEP 3: DROP FEATURES BASED ON DATA EXPLORATION SO FAR
# STEP 3a: Drop Features with Too Many MISSING VALUES, ZEROS, HIGH SKEWNESS

print('Number of rows and columns - Original     :',train.shape)
vars_to_drop = ['ps_car_03_cat','ps_car_05_cat','ps_car_10_cat','ps_ind_10_bin','ps_ind_11_bin', \
                'ps_ind_12_bin','ps_ind_13_bin','ps_ind_14']
train.drop(vars_to_drop, inplace=True, axis=1)
print('Number of rows and columns - after step 6a:',train.shape)

# STEP 3b: Drop All "_calc" Features

calc_cols = [col for col in train.columns if '_calc' in col]
if len([col for col in train.columns if '_calc' in col]) > 0:
    train = train.drop(calc_cols,axis =1)
print('Number of rows and columns - after step 6b:',train.shape)

# STEP 4: MISSING VALUE IMPUTATION
# STEP 4a: Missing Value Imputation BY MODE for "cat", "bin", and "ord" features

from collections import Counter

ps_ind_02_cat_mode = Counter(train.ps_ind_02_cat).most_common(1)[0][0]
train['ps_ind_02_cat'] = train['ps_ind_02_cat'].fillna(ps_ind_02_cat_mode)

ps_ind_04_cat_mode = Counter(train.ps_ind_04_cat).most_common(1)[0][0]
train['ps_ind_04_cat'] = train['ps_ind_04_cat'].fillna(ps_ind_04_cat_mode)

ps_ind_05_cat_mode = Counter(train.ps_ind_05_cat).most_common(1)[0][0]
train['ps_ind_05_cat'] = train['ps_ind_05_cat'].fillna(ps_ind_05_cat_mode)

ps_car_01_cat_mode = Counter(train.ps_car_01_cat).most_common(1)[0][0]
train['ps_car_01_cat'] = train['ps_car_01_cat'].fillna(ps_car_01_cat_mode)

ps_car_02_cat_mode = Counter(train.ps_car_02_cat).most_common(1)[0][0]
train['ps_car_02_cat'] = train['ps_car_02_cat'].fillna(ps_car_02_cat_mode)

ps_car_07_cat_mode = Counter(train.ps_car_07_cat).most_common(1)[0][0]
train['ps_car_07_cat'] = train['ps_car_07_cat'].fillna(ps_car_07_cat_mode)

ps_car_09_cat_mode = Counter(train.ps_car_09_cat).most_common(1)[0][0]
train['ps_car_09_cat'] = train['ps_car_09_cat'].fillna(ps_car_09_cat_mode)

ps_car_11_mode = Counter(train.ps_car_11).most_common(1)[0][0]
train['ps_car_11'] = train['ps_car_11'].fillna(ps_car_11_mode)

ps_car_14_mode = Counter(train.ps_car_14).most_common(1)[0][0]
train['ps_car_14'] = train['ps_car_14'].fillna(ps_car_14_mode)

#STEP 4b: Missing Value Imputation BY MEDIAN for "con" features

train['ps_reg_03'] = train['ps_reg_03'].fillna(train['ps_reg_03'].median())
train['ps_car_12'] = train['ps_car_12'].fillna(train['ps_car_12'].median())

# STEP 4c: Check for Missing Values, if any

cols_missing_val_train_after = train.columns[train.isnull().any()].tolist()
cols_missing_val_train_after

# STEP 5: EXPORT CLEAN DATA TO A CSV FILE
import csv

train_final_df=pd.DataFrame(train)
train_final_df

train_final_df.to_csv('/Users/sanket/Downloads/train_final.csv',mode='w', index=False)