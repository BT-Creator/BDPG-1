from sklearn.linear_model import ElasticNet

from config.regression_params import reg_params
from functions.regression_helper import split_data, print_results


def elastinet_regression(ref, target, out_name):
    ref.drop(ref.tail(1).index, inplace=True)
    ref_data, ref_prices = split_data(ref)

    # Create the regressor: reg_all
    elastic = ElasticNet(random_state=reg_params.get('random_state'))

    # Fit the regressor to the training data
    elastic.fit(ref_data, ref_prices)

    # Predict on the test data: y_pred
    y_pred = elastic.predict(target.values)

    # Export to csv
    target['SalePrice'] = y_pred
    target[['Id', 'SalePrice']].to_csv(out_name, index=False)

    # Compute and print R^2 and RMSE
    return print_results(elastic, ref_data, ref_prices, y_pred, "ElasticNet")


