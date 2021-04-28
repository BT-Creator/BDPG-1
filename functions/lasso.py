from matplotlib import pyplot as plt
from sklearn.linear_model import Lasso


def calc_lasso(train, test):
    data = train.values
    test = test
    X = data[:, :-1]
    y = test[["SalePrice"]].values
    print("@@@@@@@@@@")
    print(X)
    print("@@@@@@@@@@")
    print(y)
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
    # could not convert string to float: 'RH'
