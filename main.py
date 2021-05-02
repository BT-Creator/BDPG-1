from functions.clean import *
from functions.correlationmatrix import *
from functions.discover import *
from functions.elastinet import *
from functions.lasso import lasso_regression
from functions.regression import linear_regression
from functions.regression_helper import prep_regression_data
from functions.ridge import ridge_regression
from functions.transform import transform


def print_stage(msg):
    print("\n")
    print("#" * (len(msg) + 4))
    print("# " + msg + " #")
    print("#" * (len(msg) + 4))


# Reference data / Training Data
print_stage("Cleaning & transforming dataset_without_sale.csv (test.csv)")
ref = pd.read_csv('data/dataset_with_sale.csv')
discover_inconsistencies(ref)
ref = clean(ref)
ref = transform(ref)

# Data to Predict
print_stage("Cleaning & transforming dataset_with_sale.csv (train.csv)")
target = pd.read_csv('data/dataset_without_sale.csv')
discover_inconsistencies(target)
target = clean(target)
target = transform(target)

# Numberizing Data
int_ref = prep_regression_data(ref)
int_target = prep_regression_data(target)

# Correlation Matrix
print_stage("Generating correlation matrix's")
# generate_correlation_matrix(int_ref).show()
best = get_best_correlations(int_ref.copy())
print(best)

# Regression & prediction
best.append('Id')
model_ref = int_ref[best]
best.remove('SalePrice')
model_target = int_target[best]
print_stage("Fitting regression & prediction")
predictions = {
    'Linear Regression': linear_regression(ref.copy(), target.copy(), 'export/linear_regression.csv'),
    'Lasso regression': lasso_regression(ref.copy(), target.copy(), 'export/lasso_regression.csv'),
    'ElasticNet Regression': elastinet_regression(ref.copy(), target.copy(), 'export/elasticnet_regression.csv'),
    'Ridge Regression': ridge_regression(ref.copy(), target.copy(), 'export/ridge_regression.csv'),
    'Linear Regression (Optimized)': linear_regression(model_ref.copy(), model_target.copy(), 'export/linear_regression_optimized.csv'),
    'Lasso regression (Optimized)': lasso_regression(model_ref.copy(), model_target.copy(), 'export/lasso_regression_optimized.csv'),
    'ElasticNet Regression (Optimized)': elastinet_regression(model_ref.copy(), model_target.copy(), 'export/elasticnet_regression_optimized.csv'),
    'Ridge Regression (Optimized)': ridge_regression(model_ref.copy(), model_target.copy(), 'export/ridge_regression_optimized.csv')
}

best_prediction = None
r2 = 0
for key, value in predictions.items():
    if value > r2:
        best_prediction = key
        r2 = value
print("The regression method {} has the best prediction with a R^2 of {}".format(
    best_prediction,
    predictions.get(best_prediction)
))
