from functions.clean import *
from functions.discover import *
from functions.transform import transform
from functions.correlationmatrix import *
from functions.ridgeregression import *


def print_stage(msg):
    print("\n")
    print("#" * (len(msg) + 4))
    print("# " + msg + " #")
    print("#" * (len(msg) + 4))


# Train
print_stage("Cleaning & transforming train.csv")
train = pd.read_csv('./data/train.csv')
discover_inconsistencies(train)
train = clean(train)
discover_inconsistencies(train)
train = transform(train)

# Clean
print_stage("Cleaning & transforming test.csv")
test = pd.read_csv('./data/test.csv')
discover_inconsistencies(test)
test = clean(test)
discover_inconsistencies(test)
test = transform(test)

# Correlation Matrix
print_stage("Generating a correlation matrix for train.csv")
generate_correlation_matrix(train).show()
get_best_correlations(train)

# Ridge Regression
print_stage("Getting the ridge regression")
ridge_regression(train)