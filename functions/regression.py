import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score

from config.regression_params import reg_params
from functions.clean import *
from functions.regression_helper import prep_regression_data, split_data, print_results


def linear_regression(train, test):
    train = prep_regression_data(train)
    train[reg_params.get('target_column')] = 0
    test = prep_regression_data(test)
    data = pd.concat([test, train])
    X, y = split_data(data)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=reg_params.get('test_size'),
        random_state=reg_params.get('random_state'),
        shuffle=reg_params.get('shuffle')
    )
    print(X_train)
    print(X_test)
    print(y_train)
    print(y_test)

    # Create the regressor: l_reg
    l_reg = LinearRegression()

    # Perform 3-fold CV
    cvscores_3 = cross_val_score(l_reg, X_train, y_train, cv=4)
    print(np.mean(cvscores_3))

    # Fit the regressor to the training data
    l_reg.fit(X_train, y_train)

    # Predict on the test data: y_pred
    print(np.all(np.isnan(X_test)))
    y_pred = l_reg.predict(X_test)

    # Compute and print R^2 and RMSE
    return print_results(l_reg, X_test, y_test, y_pred, "Linear")
