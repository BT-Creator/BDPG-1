from functions.clean import *
from functions.correlationmatrix import *
from functions.discover import *
from functions.regression.elastinet import elastinet_regression
from functions.regression.lasso import lasso_regression
from functions.regression.linear import linear_regression
from functions.regression.regression_helper import prep_regression_data
from functions.regression.ridge import ridge_regression
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
best_pearson = get_best_correlations(int_ref.copy(), 'pearson')
best_kendall = get_best_correlations(int_ref.copy(), 'kendall')
best_spearman = get_best_correlations(int_ref.copy(), 'spearman')
print(best_pearson)
print(best_kendall)
print(best_spearman)

# Regression & prediction
print_stage("Fitting regression & prediction")

# Prep ref data
best_pearson.append('Id')
best_kendall.append('Id')
best_spearman.append('Id')
model_ref_pearson = int_ref[best_pearson]
model_ref_kendall = int_ref[best_kendall]
model_ref_spearman = int_ref[best_spearman]

# Prep target data
best_pearson.remove('SalePrice')
best_kendall.remove('SalePrice')
best_spearman.remove('SalePrice')
model_target_pearson = int_target[best_pearson]
model_target_kendall = int_target[best_kendall]
model_target_spearman = int_target[best_spearman]

# Make predictions
predictions = {
    'Linear Regression | Non-Optimized': linear_regression(
        ref.copy(),
        target.copy(),
        'export/linear/linear_regression.csv'
    ),
    'Lasso Regression | Non-Optimized': lasso_regression(
        ref.copy(),
        target.copy(),
        'export/lasso/lasso_regression.csv'
    ),
    'ElasticNet Regression | Non-Optimized': elastinet_regression(
        ref.copy(),
        target.copy(),
        'export/elasticNet/elasticnet_regression.csv'
    ),
    'Ridge Regression | Non-Optimized': ridge_regression(
        ref.copy(),
        target.copy(),
        'export/ridge/ridge_regression.csv'
    ),
    'Linear Regression | Optimized - Pearson': linear_regression(
        model_ref_pearson.copy(),
        model_target_pearson.copy(),
        'export/linear/linear_regression_optimized_pearson.csv'
    ),
    'Lasso Regression | Optimized - Pearson': lasso_regression(
        model_ref_pearson.copy(),
        model_target_pearson.copy(),
        'export/lasso/lasso_regression_optimized_pearson.csv'
    ),
    'ElasticNet Regression | Optimized - Pearson': elastinet_regression(
        model_ref_pearson.copy(),
        model_target_pearson.copy(),
        'export/elasticNet/elasticnet_regression_optimized_pearson.csv'
    ),
    'Ridge Regression | Optimized - Pearson': ridge_regression(
        model_ref_pearson.copy(),
        model_target_pearson.copy(),
        'export/ridge/ridge_regression_optimized_pearson.csv'
    ),
    'Linear Regression | Optimized - Kendall': linear_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/linear/linear_regression_optimized_kendall.csv'
    ),
    'Lasso Regression | Optimized - Kendall': lasso_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/lasso/lasso_regression_optimized_kendall.csv'
    ),
    'ElasticNet Regression | Optimized - Kendall': elastinet_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/elasticNet/elasticnet_regression_optimized_kendall.csv'
    ),
    'Ridge Regression | Optimized - Kendall': ridge_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/ridge/ridge_regression_optimized_kendall.csv'
    ),
    'Linear Regression | Optimized - Spearman': linear_regression(
        model_ref_spearman.copy(),
        model_target_spearman.copy(),
        'export/linear/linear_regression_optimized_spearman.csv'
    ),
    'Lasso Regression | Optimized - Spearman': lasso_regression(
        model_ref_spearman.copy(),
        model_target_spearman.copy(),
        'export/lasso/lasso_regression_optimized_spearman.csv'
    ),
    'ElasticNet Regression | Optimized - Spearman': elastinet_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/elasticNet/elasticnet_regression_optimized_spearman.csv'
    ),
    'Ridge Regression | Optimized - Spearman': ridge_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/ridge/ridge_regression_optimized_spearman.csv'
    )
}

best_prediction = None
rsme = predictions.get('Linear Regression | Non-Optimized')
for key, value in predictions.items():
    if value < rsme:
        best_prediction = key
        rsme = value
print("The regression method {} has the best prediction with a RMSE of {}".format(
    best_prediction,
    predictions.get(best_prediction)
))
