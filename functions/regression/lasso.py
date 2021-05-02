from sklearn.linear_model import Lasso

from functions.regression.regression_helper import print_results, split_data


def lasso_regression(ref, target, out_name):
    ref.drop(ref.tail(1).index, inplace=True)
    ref_data, ref_prices = split_data(ref)

    # Create the regressor: lasso
    lasso = Lasso(alpha=0.4, normalize=True)

    # Fit the regressor to the training data
    lasso.fit(ref_data, ref_prices)

    # Predict on the test data: y_pred
    y_pred = lasso.predict(target.values)

    # Export to csv
    target['SalePrice'] = y_pred
    target[['Id', 'SalePrice']].to_csv(out_name, index=False)

    # Compute and print R^2 and RMSE
    return print_results(lasso, ref_data, ref_prices, y_pred, "lasso")
