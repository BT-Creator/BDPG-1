from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

from config.regression_params import reg_params
from functions.regression import prep_regression_data, split_data
from functions.regression_helper import print_results


def ridge_regression(train):
    prep = prep_regression_data(train)
    X, y = split_data(prep)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=reg_params.get('test_size'),
        random_state=reg_params.get('random_state')
    )

    # Create the regressor: reg_all
    rr = Ridge(alpha=1)

    # Fit the regressor to the training data
    rr.fit(X_train, y_train)

    # Predict on the test data: y_pred
    y_pred = rr.predict(X_test)

    # Compute and print R^2 and RMSE
    return print_results(rr, X_test, y_test, y_pred, "Ridge")
