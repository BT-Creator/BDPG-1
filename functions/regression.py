from sklearn.linear_model import LinearRegression

from functions.regression_helper import split_data, print_results


def linear_regression(ref, target, out_name):
    ref.drop(ref.tail(1).index, inplace=True)
    ref_data, ref_prices = split_data(ref)

    # Create the regressor: l_reg
    l_reg = LinearRegression()

    # Fit the regressor to the training data
    l_reg.fit(ref_data, ref_prices)

    # Predict on the test data: y_pred
    y_pred = l_reg.predict(target.values)

    # Export to csv
    target['SalePrice'] = y_pred
    target[['Id', 'SalePrice']].to_csv(out_name, index=False)

    # Compute and print R^2 and RMSE
    return print_results(l_reg, ref_data, ref_prices, y_pred, "Linear")
