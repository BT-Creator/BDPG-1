import pandas as pd
from skimage.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from config.regression_params import reg_params
from functions.clean import *
from functions.discover import *


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def split_data(train, test):
    train_data = train
    test_data = test[reg_params.get('target_column')].values
    ref_prices = test.drop(reg_params.get('target_column'), axis=1).values
    return train_data, test_data, ref_prices


def linear_regression(test, train):
    xtrain = prep_regression_data(train)
    ytrain = np.log(xtrain.pop('SalePrice')).values
    xtrain = xtrain.values

    X_train, X_test, y_train, y_test = train_test_split(xtrain, ytrain, test_size=0.3, random_state=42)

    # Create the regressor: reg_all
    reg_all = LinearRegression()

    # Fit the regressor to the training data
    reg_all.fit(X_train, y_train)

    # Predict on the test data: y_pred
    y_pred = reg_all.predict(X_test)

    # Compute and print R^2 and RMSE
    print("===== Linear regresion =====")
    print("R^2: {}".format(reg_all.score(X_test, y_test)))
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Error: {}".format(rmse))
    print("===== End Linear regresion =====")
    print()



def prep_regression_data(df):
    for key in categorical_values.keys():
        if df[key].isnull().values.any():
            df[key] = df[key].cat.add_categories(-1).fillna(-1)
            df[key] = df[key].cat.remove_categories(None)
        df[key] = df[key].cat.reorder_categories(df[key].unique(), ordered=True)
        df[key] = df[key].cat.codes
    return df
