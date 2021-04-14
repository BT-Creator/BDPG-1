import pandas as pd
from data.config import *
from functions.clean import *
from functions.discover import *
from functions.transform import transform

# Train
train = pd.read_csv('./data/train.csv')
discover_inconsistencies(train, categorical_values)
train = clean(train)
train = transform(train)
# TODO: Remember adding SoldDate to documentation

# Clean
test = pd.read_csv('./data/test.csv')
discover_inconsistencies(test, categorical_values)
test = clean(test)
discover_inconsistencies(test, categorical_values)
print(test['BsmtFullBath'].isna().values.any())
