from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

from config.regression_params import reg_params
from functions.regression import prep_regression_data, split_data
from functions.regression_helper import print_results


def ridge_regression(ref, target):
    prepped_ref = prep_regression_data(ref)
    prepped_target = prep_regression_data(target)
    prepped_ref.drop(ref.tail(1).index, inplace=True)
    ref_data, ref_prices = split_data(prepped_ref)

    # Create the regressor: reg_all
    rr = Ridge(alpha=1)

    # Fit the regressor to the training data
    rr.fit(ref_data, ref_prices)

    # Predict on the test data: y_pred
    y_pred = rr.predict(prepped_target.values)

    # Compute and print R^2 and RMSE
    return print_results(rr, ref_data, ref_prices, y_pred, "Ridge")
