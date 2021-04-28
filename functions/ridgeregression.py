# Import necessary modules
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
import pandas as pd


def ridge_regression(df):
    data = df.values
    print(data)
    # X, y = data[:, :-1], data[:, -1]
    # model = Ridge(alpha=1.0)
    # cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
    # scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
    # scores = np.absolute(scores)
    # return np.mean(scores), np.std(scores)


