from networkx.drawing.tests.test_pylab import plt
from skimage.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from functions.clean import *
from functions.discover import *
from functions.transform import transform
from functions.regression import prep_regression_data, split_data
from sklearn.linear_model import ElasticNet, Ridge, ElasticNetCV, Lasso
from sklearn.datasets import make_regression
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

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
    print("===== Lasso regresion =====")
    print("R^2: {}".format(lasso.score(X_test, y_test)))
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Error: {}".format(rmse))
    print("===== End Lasso regresion =====")
    print()
