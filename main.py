from functions.clean import *
from functions.correlationmatrix import *
from functions.discover import *
from functions.elastinet import *
from functions.lasso import lasso_regression
from functions.regression import linear_regression
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
cleaned_ref = clean(ref)
transformed_ref = transform(ref)

# Data to Predict
print_stage("Cleaning & transforming dataset_with_sale.csv (train.csv)")
target = pd.read_csv('data/dataset_without_sale.csv')
discover_inconsistencies(target)
cleaned_target = clean(target)
transformed_target = transform(target)

# Correlation Matrix
# print_stage("Generating correlation matrix's")
# generate_correlation_matrix(train).show()
# get_best_correlations(train)
# generate_correlation_matrix(train).show()
# get_best_correlations(train)

# Regression & prediction
print_stage("Fitting regression & prediction")
predictions = {
    'Linear Regression': linear_regression(transformed_ref.copy(), transformed_target.copy()),
    'Lasso regression': lasso_regression(transformed_ref.copy(), transformed_target.copy()),
    'ElasticNet Regression': elastinet_regression(transformed_ref.copy(), transformed_target.copy()),
    'Ridge Regression': ridge_regression(transformed_ref.copy(), transformed_target.copy())
}
best_prediction = None
r2 = 0
for key, value in predictions.items():
    if value > r2:
        best_prediction = key
print("The regression method {} has the best prediction with a R^2 of {}".format(
    best_prediction,
    predictions.get(best_prediction)
))
