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
        values = categorical_values.get(key)
        if train_data[key].isnull().values.any():
            values = replace_None(categorical_values.get(key))
            train_data[key] = train_data[key].cat.add_categories(-1).fillna(-1)
            train_data[key] = train_data[key].cat.remove_categories(None)
        print("############ " + key + " ############")
        print(train_data[key].unique())
        print(train_data[key].isnull().values.any())
        print(values)
        print(len(train_data[key].unique()) == len(values))
        train_data[key] = train_data[key].cat.reorder_categories(train_data[key].unique(), ordered=True)
        train_data[key] = train_data[key].cat.codes
    print(train_data[list(categorical_values.keys())])
    # l_reg.fit(train_data, ref_prices)
    # print(l_reg.predict(train_data))


def replace_None(array):
    for n, value in enumerate(array):
        if value is None:
            array[n] = -1
    return array
