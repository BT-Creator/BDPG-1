import pandas as pd
from sklearn.linear_model import LinearRegression

from config.clean_params import categorical_values
from config.regression_params import reg_params


def split_data(train, test):
    train_data = train
    test_data = test[reg_params.get('target_column')].values
    ref_prices = test.drop(reg_params.get('target_column'), axis=1).values
    return train_data, test_data, ref_prices


def linear_regression(train_data, test_data, ref_prices):
    l_reg = LinearRegression()
    for key in categorical_values.keys():
        print(train_data[key].unique())
        print(train_data[key].isnull().values.any())
        print(categorical_values.get(key))
        print(len(train_data[key].unique()) == len(categorical_values.get(key)))
        train_data[key] = train_data[key].cat.reorder_categories(train_data[key].unique(), ordered=True)
    print(train_data[list(categorical_values.keys())])
    # l_reg.fit(train_data, ref_prices)
    # print(l_reg.predict(train_data))

