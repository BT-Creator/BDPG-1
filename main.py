import pandas as pd

train = pd.read_csv('./data/train.csv')

for column in train:
    nan = train[column].isnull().values.any()
    if (nan == True):
        print(column)
        print(nan)
        print("-"*80)

#for column in train:
#    train.sort_values(column)
#    print(column)
#    print('-'*80)
#    print(train[column].unique())

