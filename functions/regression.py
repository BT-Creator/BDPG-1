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
    train_data = prep_regression_data(train_data)
    #l_reg.fit(train_data.values, ref_prices)
    # print(l_reg.predict(train_data))


def prep_regression_data(df):
    for key in categorical_values.keys():
        if df[key].isnull().values.any():
            df[key] = df[key].cat.add_categories(-1).fillna(-1)
            df[key] = df[key].cat.remove_categories(None)
        df[key] = df[key].cat.reorder_categories(df[key].unique(), ordered=True)
        df[key] = df[key].cat.codes
    return df
