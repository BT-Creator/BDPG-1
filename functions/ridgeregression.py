# Import necessary modules
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
import pandas as pd


def ridge_regression(train, test):
    data = train.values
    test = test
    X = data[:, :-1]
    y = test[["SalePrice"]].values
    print(X,y)
    test_x = test
    model = Ridge(alpha=0.1)
    model.fit(train_x, train_y)
    test_y = model.predict(test_x)
    return model.score(test_x, test_y)


