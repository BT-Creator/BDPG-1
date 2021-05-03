from functions.clean import *
from functions.correlation_matrix import *
from functions.discover import *
from functions.regression.elastinet import elastinet_regression
from functions.regression.lasso import lasso_regression
from functions.regression.linear import linear_regression
from functions.regression.regression_helper import prep_regression_data, add_missing_possibilities, \
    post_best_predictions
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
# Adding Number data
int_ref = prep_regression_data(ref.copy())
int_target = prep_regression_data(target.copy())
# Checking if all dummies are included in dataset and filling in missing dummies
int_ref_length = len(int_ref.columns)
int_target_length = len(int_target.columns)
missing_columns_target = int_ref[int_ref.columns.difference(int_target.columns.tolist())].columns.tolist()
missing_columns_target.remove('SalePrice')
int_target = add_missing_possibilities(int_target, missing_columns_target)
missing_columns_ref = int_target[int_target.columns.difference(int_ref.columns.tolist())].columns.tolist()
int_ref = add_missing_possibilities(int_ref, missing_columns_ref)

# Correlation Matrix
print_stage("Generating correlation matrix's")
corr_df = prep_correlation_data(ref)
corr_pearson = get_best_correlations(corr_df.copy(), 'pearson')
corr_kendall = get_best_correlations(corr_df.copy(), 'kendall')
corr_spearman = get_best_correlations(corr_df.copy(), 'spearman')
generate_correlation_matrix(corr_df, corr_pearson, "Pearson Correlation matrix").show()
generate_correlation_matrix(corr_df, corr_kendall, "Kendall Correlation matrix").show()
generate_correlation_matrix(corr_df, corr_spearman, "Spearman Correlation matrix").show()

# Regression & prediction
print_stage("Fitting regression & prediction")

# Prep ref data
corr_pearson = get_best_correlations(int_ref.copy(), 'pearson')
corr_kendall = get_best_correlations(int_ref.copy(), 'kendall')
corr_spearman = get_best_correlations(int_ref.copy(), 'spearman')
corr_pearson.append('Id')
corr_kendall.append('Id')
corr_spearman.append('Id')
model_ref_pearson = int_ref[corr_pearson]
model_ref_kendall = int_ref[corr_kendall]
model_ref_spearman = int_ref[corr_spearman]

# Prep target data
corr_pearson.remove('SalePrice')
corr_kendall.remove('SalePrice')
corr_spearman.remove('SalePrice')
model_target_pearson = int_target[corr_pearson]
model_target_kendall = int_target[corr_kendall]
model_target_spearman = int_target[corr_spearman]

# Make predictions
predictions_linear = {
    'Linear Regression | Non-Optimized': linear_regression(
        int_ref.copy(),
        int_target.copy(),
        'export/linear/linear_regression.csv'
    ),
    'Linear Regression | Optimized - Pearson': linear_regression(
        model_ref_pearson.copy(),
        model_target_pearson.copy(),
        'export/linear/linear_regression_optimized_pearson.csv'
    ),
    'Linear Regression | Optimized - Kendall': linear_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/linear/linear_regression_optimized_kendall.csv'
    ),
    'Linear Regression | Optimized - Spearman': linear_regression(
        model_ref_spearman.copy(),
        model_target_spearman.copy(),
        'export/linear/linear_regression_optimized_spearman.csv'
    ),
}
predictions_ridge = {
    'Ridge Regression | Non-Optimized': ridge_regression(
        int_ref.copy(),
        int_target.copy(),
        'export/ridge/ridge_regression.csv'
    ),
    'Ridge Regression | Optimized - Pearson': ridge_regression(
        model_ref_pearson.copy(),
        model_target_pearson.copy(),
        'export/ridge/ridge_regression_optimized_pearson.csv'
    ),
    'Ridge Regression | Optimized - Kendall': ridge_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/ridge/ridge_regression_optimized_kendall.csv'
    ),
    'Ridge Regression | Optimized - Spearman': ridge_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/ridge/ridge_regression_optimized_spearman.csv'
    )
}
predictions_elasticnet = {
    'ElasticNet Regression | Non-Optimized': elastinet_regression(
        int_ref.copy(),
        int_target.copy(),
        'export/elasticNet/elasticnet_regression.csv'
    ),
    'ElasticNet Regression | Optimized - Pearson': elastinet_regression(
        model_ref_pearson.copy(),
        model_target_pearson.copy(),
        'export/elasticNet/elasticnet_regression_optimized_pearson.csv'
    ),
    'ElasticNet Regression | Optimized - Kendall': elastinet_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/elasticNet/elasticnet_regression_optimized_kendall.csv'
    ),
    'ElasticNet Regression | Optimized - Spearman': elastinet_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/elasticNet/elasticnet_regression_optimized_spearman.csv'
    )
}
predictions_lasso = {
    'Lasso Regression | Non-Optimized': lasso_regression(
        int_ref.copy(),
        int_target.copy(),
        'export/lasso/lasso_regression.csv'
    ),
    'Lasso Regression | Optimized - Pearson': lasso_regression(
        model_ref_pearson.copy(),
        model_target_pearson.copy(),
        'export/lasso/lasso_regression_optimized_pearson.csv'
    ),
    'Lasso Regression | Optimized - Kendall': lasso_regression(
        model_ref_kendall.copy(),
        model_target_kendall.copy(),
        'export/lasso/lasso_regression_optimized_kendall.csv'
    ),
    'Lasso Regression | Optimized - Spearman': lasso_regression(
        model_ref_spearman.copy(),
        model_target_spearman.copy(),
        'export/lasso/lasso_regression_optimized_spearman.csv'
    )
}

post_best_predictions(predictions_linear)
post_best_predictions(predictions_lasso)
post_best_predictions(predictions_elasticnet)
post_best_predictions(predictions_ridge)
