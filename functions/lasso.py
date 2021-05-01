from skimage.metrics import mean_squared_error
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from functions.clean import *
from functions.regression import prep_regression_data, split_data


def lasso_regression(train):
    prep = prep_regression_data(train)
    X, y = split_data(prep)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

    # Create the regressor: reg_all
    lasso = Lasso(alpha=0.4, normalize=True)

    # Fit the regressor to the training data
    lasso.fit(X_train, y_train)

    # # Predict on the test data: y_pred
    y_pred = lasso.predict(X_test)

    # Compute and print R^2 and RMSE
    print("===== Lasso regression =====")
    print("R^2: {}".format(lasso.score(X_test, y_test)))
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Error: {}".format(rmse))
    print("===== End Lasso regression =====")
    print()
