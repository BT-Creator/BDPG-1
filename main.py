import pandas as pd
from functions.clean import *
from functions.discover import *
from functions.transform import transform

# Train
train = pd.read_csv('./data/train.csv')
discover_inconsistencies(train)
train = clean(train)
discover_inconsistencies(train)
train = transform(train)
# TODO: Remember adding SoldDate to documentation

# Clean
test = pd.read_csv('./data/test.csv')
discover_inconsistencies(test)
test = clean(test)
discover_inconsistencies(test)
print(test['BsmtFullBath'].isna().values.any())
