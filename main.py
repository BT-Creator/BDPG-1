import pandas as pd
from data.config import *
from functions.clean import *
from functions.discover import *

# Discover Phase
from functions.transform import convert_to_date

train = pd.read_csv('./data/train.csv')
discover_inconsistencies(train, allowed_values)

# Cleaning Phase
train.loc[train['LotFrontage'] == -1, 'LotFrontage'] = apply_avg(train, 'LotFrontage', -1)
train.loc[train['MSZoning'] == "C (all)", 'MSZoning'] = replace_string(train, "MSZoning", "C (all)", "C")
train.loc[train['BldgType'] == "Twnhs", 'BldgType'] = replace_string(train, "BldgType", "Twnhs", "TwnhsI")
train.loc[train['BldgType'] == "2fmCon", 'BldgType'] = replace_string(train, "BldgType", "2fmCon", "2FmCon")
train.loc[train['Exterior2nd'] == "CmentBd", "Exterior2nd"] = replace_string(train, "Exterior2nd", "CmentBd", "CemntBd")
train.loc[train['Exterior2nd'] == "Brk Cmn", "Exterior2nd"] = replace_string(train, "Exterior2nd", "Brk Cmn", "BrkComm")
train.loc[train['Exterior2nd'] == "Wd Shng", "Exterior2nd"] = replace_string(train, "Exterior2nd", "Wd Shng", "WdShing")
train.loc[train['MasVnrType'] == "None", 'MasVnrType'] = replace_string(train, "MasVnrType", "None", None)
train.loc[train['MasVnrArea'] == -1, 'MasVnrArea'] = apply_avg(train, 'MasVnrArea', -1)
train.loc[train['GarageYrBlt'] == -1, 'GarageYrBlt'] = apply_avg(train, 'GarageYrBlt', -1)

# Verifying
discover_inconsistencies(train, allowed_values)

# Transform
train['CentralAir'] = train['CentralAir'].astype('bool')
train[list(allowed_values.keys())] = train[list(allowed_values.keys())].astype('category')
train[float_columns] = train[float_columns].astype(float)
train[date_columns.get('year')] = convert_to_date(train, date_columns.get('year'), '%Y')
print(train.dtypes)
