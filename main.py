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


# Target
print_stage("Cleaning & transforming dataset_with_sale.csv")
target = pd.read_csv('data/dataset_without_sale.csv')
discover_inconsistencies(target)
target = clean(target)
target = transform(target)

# Test
print_stage("Cleaning & transforming dataset_without_sale.csv")
test = pd.read_csv('data/dataset_with_sale.csv')
discover_inconsistencies(test)
test = clean(test)
test = transform(test)

# Correlation Matrix
# print_stage("Generating correlation matrix's")
# generate_correlation_matrix(train).show()
# get_best_correlations(train)
# generate_correlation_matrix(train).show()
# get_best_correlations(train)

# Regression & prediction
print_stage("Fitting regression & prediction")
predictions = {
    'Linear Regression': linear_regression(target.copy(), test.copy()),
    'ElasticNet Regression': elastinet_regression(test.copy()),
    'Ridge Regression': ridge_regression(test.copy()),
    'Lasso regression': lasso_regression(test.copy())
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
