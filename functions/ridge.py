from sklearn.linear_model import Ridge

from functions.regression import split_data
from functions.regression_helper import print_results


def ridge_regression(ref, target, out_name):
    ref.drop(ref.tail(1).index, inplace=True)
    ref_data, ref_prices = split_data(ref)

    # Create the regressor: reg_all
    rr = Ridge(alpha=1)

    # Fit the regressor to the training data
    rr.fit(ref_data, ref_prices)

    # Predict on the test data: y_pred
    y_pred = rr.predict(target.values)

    # Export to csv
    target['SalePrice'] = y_pred
    target[['Id', 'SalePrice']].to_csv(out_name, index=False)

    # Compute and print R^2 and RMSE
    return print_results(rr, ref_data, ref_prices, y_pred, "Ridge")
