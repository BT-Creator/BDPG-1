import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


def calc_lasso(df):
    print("#####################################")
    print("############### LASSO ###############")
    print("#####################################")
    # Import Lasso
    from sklearn.linear_model import Lasso
    # Instantiate a lasso regressor: lasso
    lasso = Lasso(alpha=0.4, normalize=True)
    y = df['SaleCondition'].values
    X = df['SalePrice'].values
    # Print the dimensions of X and y before reshaping
    print("Dimensions of y before reshaping: {}".format(y.shape))
    print("Dimensions of X before reshaping: {}".format(X.shape))
    # Reshape X and y
    y_reshaped = y.reshape(-1, 1)
    X_reshaped = X.reshape(-1, 1)
    # Print the dimensions of X and y after reshaping
    print("Dimensions of y after reshaping: ", y_reshaped.shape)
    print("Dimensions of X after reshaping: ", X_reshaped.shape)
    # Create the regressor: reg
    reg = LinearRegression()
    # Create the prediction space
    prediction_space = np.linspace(min(X), max(X)).reshape(-1, 1)
    # Fit the model to the data
    reg.fit(X, y)
    # Compute predictions over the prediction space: y_pred
    y_pred = reg.predict(prediction_space)
    # Print R^2
    print(reg.score(X, y))
    # Plot regression line
    plt.plot(prediction_space, y_pred, color='black', linewidth=3)
    plt.show()