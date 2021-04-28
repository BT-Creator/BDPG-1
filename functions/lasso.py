import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso


def calc_lasso(train, test):
    data = train.values
    test = test.values
    X, y = data[:, :-1], data[:, -1]
    # Instantiate a lasso regressor: lasso
    lasso = Lasso(alpha=0.1, normalize=True)
    # Fit the regressor to the data
    lasso.fit(X, y)
    # Compute and print the coefficients
    lasso_coef = lasso.coef_
    print(lasso_coef)
    # Plot the coefficients
    plt.plot(range(len(train.columns)), lasso_coef)
    plt.xticks(range(len(train.columns)), train.columns.values, rotation=60)
    plt.margins(0.02)
    plt.show()
