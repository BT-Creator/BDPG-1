import pandas as pd
from data.allowed_values import allowed_values
from functions.clean import *
from functions.discover import discover_inconsistencies

# Discover Phase
train = pd.read_csv('./data/train.csv')
discover_inconsistencies(train, allowed_values)

# Cleaning Phase
apply_avg(train, 'LotFrontage', -1)
