import pandas as pd
from data.allowed_values import allowed_values

train = pd.read_csv('./data/train.csv')

for column in train:
    if (column != 'Id') and column in allowed_values:
        illegal_values = train[~train[column].isin(allowed_values[column])][column]
        illegal_rows = illegal_values.count()
        if illegal_rows > 0:
            print("There are", illegal_rows, "rows with illegal string values in column", column)
            print("-" * 80)
    elif column != 'Id':
        train[column] = train[column].fillna(-1).astype(int)
        illegal_rows = train[train[column] == -1][column].count()
        if illegal_rows > 0:
            print("There are", illegal_rows, "rows with NaN values in column", column)
            print("-"*80)