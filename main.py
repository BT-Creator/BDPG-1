import pandas as pd
from data.allowed_values import allowed_values
from functions import discover_inconsistencies

train = pd.read_csv('./data/train.csv')
discover_inconsistencies(train, allowed_values)
