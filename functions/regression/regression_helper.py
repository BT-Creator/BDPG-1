import numpy as np
import pandas as pd
from skimage.metrics import mean_squared_error
from sklearn.metrics import mean_squared_error

from config.regression_params import reg_params
from functions.discover import *


def split_data(train):
    y = train[reg_params.get('target_column')].values.reshape(-1, 1)
    X = train.drop(reg_params.get('target_column'), axis=1).values
    return X, y


def prep_regression_data(df):
    for array in chained_columns.values():
        for column in array:
            if df[column].dtype.name is not 'category':
                df[column].fillna(-1, inplace=True)
    df['CentralAir'] = df['CentralAir'].astype(int)
    df = pd.get_dummies(df, dummy_na=True)
    return df


def replace_categorical_na(df, key):
    if df[key].isnull().values.any():
        df[key] = df[key].cat.add_categories(-1).fillna(-1)
        df[key] = df[key].cat.remove_categories(None)
    df[key] = df[key].cat.reorder_categories(df[key].unique(), ordered=True)
    df[key] = df[key].cat.codes


def print_results(regression, X_test, y_test, y_pred, regression_name):
    print("===== {} regression =====".format(regression_name))
    r2 = regression.score(X_test, y_test)
    print("R^2: {}".format(r2))
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Error: {}".format(rmse))
    print("===== End {} regression ===== \n".format(regression_name))
    return rmse


def add_missing_possibilities(df, columns):
    for column in columns:
        df[column] = 0
        df[column].astype('uint8')
    return df
