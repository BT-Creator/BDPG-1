import pandas as pd
from skimage.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, cross_val_score

from config.regression_params import reg_params
from functions.clean import *
from functions.discover import *


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from functions.regression_helper import prep_regression_data, split_data


def linear_regression(train):
    prep = prep_regression_data(train)
    X, y = split_data(prep)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

    # Create the regressor: reg_all
    reg_all = LinearRegression()

    # Perform 3-fold CV
    cvscores_3 = cross_val_score(reg_all, X_train, y_train, cv=4)
    print(np.mean(cvscores_3))



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
