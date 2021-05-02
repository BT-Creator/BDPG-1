from sklearn.linear_model import Lasso

from functions.regression import prep_regression_data, split_data
from functions.regression_helper import print_results


def lasso_regression(ref, target):
    prepped_ref = prep_regression_data(ref)
    prepped_target = prep_regression_data(target)
    prepped_ref.drop(ref.tail(1).index, inplace=True)
    ref_data, ref_prices = split_data(prepped_ref)

    # Create the regressor: lasso
    lasso = Lasso(alpha=0.4, normalize=True)

    # Fit the regressor to the training data
    lasso.fit(ref_data, ref_prices)

    # # Predict on the test data: y_pred
    y_pred = lasso.predict(prepped_target.values)

    # Compute and print R^2 and RMSE
    return print_results(lasso, ref_data, ref_prices, y_pred, "Lasso")
