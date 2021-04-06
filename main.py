import pandas as pd
from data.allowed_values import allowed_values
from functions.clean import *
from functions.discover import discover_inconsistencies

# Discover Phase
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
# Verifying
discover_inconsistencies(train, allowed_values)
