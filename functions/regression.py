import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

from config.regression_params import reg_params


def split_data(train, test):
    y_train = train[reg_params.get('target_column')].values
    X_train = train.drop(reg_params.get('target_column'), axis=1).values
    X_test = test.values
    y_test = None
    return X_train, X_test, y_train, y_test


def calc_ridge(X_train, y_train):
    alpha_space = np.logspace(-4, 0, 50)
    ridge_scores = []
    ridge_scores_std = []
    ridge = Ridge()
    for alpha in alpha_space:
        ridge.alpha = alpha
        ridge_cv_scores = cross_val_score(ridge, X_train, y_train, reg_params.get('cv'))
        ridge_scores.append(np.mean(ridge_cv_scores))
        ridge_scores_std.append(np.std(ridge_cv_scores))
    display_plot(ridge_scores, ridge_scores_std)


def display_plot(cv_scores, cv_scores_std):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(cv_scores)

    std_error = cv_scores_std / np.sqrt(10)

    ax.fill_between(cv_scores + std_error, cv_scores - std_error, alpha=0.2)
    ax.set_ylabel('CV Score +/- Std Error')
    ax.set_xlabel('Alpha')
    ax.axhline(np.max(cv_scores), linestyle='--', color='.5')
    ax.set_xscale('log')
    plt.show()
