from functions.clean import *
from functions.discover import *
from functions.transform import transform
from functions.regression import split_data


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

# Regression
X_train, X_test, y_train, y_test = split_data(train, test)
print(X_train)
print(X_test)
print(y_train)
print(y_test)
