import pandas as pd
import numpy as np
from data.allowed_values import allowed_values

train = pd.read_csv('./data/train.csv')

for column in train:
    if (column != 'Id') and column in allowed_values:
        illegal_values = train[~train[column].isin(allowed_values[column])][column]
        illegal_rows = illegal_values.count()
        if illegal_rows > 0:
            print("There are", illegal_rows, "rows with illegal values in column", column)
