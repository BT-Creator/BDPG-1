import pandas as pd
from data.config import *
from functions.clean import *
from functions.discover import *
from functions.transform import transform

# Train
train = pd.read_csv('./data/train.csv')
discover_inconsistencies(train, allowed_values)
train = clean(train)
train = transform(train)
# TODO: Remember adding SoldDate to documentation

# Clean
