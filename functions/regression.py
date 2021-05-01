from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score

from config.regression_params import reg_params
from functions.clean import *
from functions.regression_helper import prep_regression_data, split_data, print_results


def linear_regression(train):
    prep = prep_regression_data(train)
    X, y = split_data(prep)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=reg_params.get('test_size'),
        random_state=reg_params.get('random_state')
    )

    # Create the regressor: l_reg
    l_reg = LinearRegression()

    # Perform 3-fold CV
    cvscores_3 = cross_val_score(l_reg, X_train, y_train, cv=4)
    print(np.mean(cvscores_3))

    # Fit the regressor to the training data
    l_reg.fit(X_train, y_train)

    # Predict on the test data: y_pred
    y_pred = l_reg.predict(X_test)

    # Compute and print R^2 and RMSE
    return print_results(l_reg, X_test, y_test, y_pred, "Linear")
