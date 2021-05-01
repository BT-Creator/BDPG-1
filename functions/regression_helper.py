from skimage.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from config.regression_params import reg_params
from functions.clean import *
from functions.discover import *


def split_data(train):
    y = train[reg_params.get('target_column')].values.reshape(-1, 1)
    X = train.drop(reg_params.get('target_column'), axis=1).values
    return X, y


def test_reg(train):
    prep = prep_regression_data(train)
    print(prep)
    X, y = split_data(prep)
    print("X", X)
    print("Y", y)
    print(train.dtypes)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

    # Create the regressor: reg_all
    reg_all = LinearRegression()

    # Fit the regressor to the training data
    reg_all.fit(X_train, y_train)

    # Predict on the test data: y_pred
    y_pred = reg_all.predict(X_test)

    # Compute and print R^2 and RMSE
    print("R^2: {}".format(reg_all.score(X_test, y_test)))
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Error: {}".format(rmse))


def prep_regression_data(df):
    for key in categorical_values.keys():
        if df[key].isnull().values.any():
            df[key] = df[key].cat.add_categories(-1).fillna(-1)
            df[key] = df[key].cat.remove_categories(None)
        df[key] = df[key].cat.reorder_categories(df[key].unique(), ordered=True)
        df[key] = df[key].cat.codes
    return df


def print_results(regression, X_test, y_test, y_pred, regression_name):
    print("===== {} regression =====".format(regression_name))
    r2 = regression.score(X_test, y_test)
    print("R^2: {}".format(r2))
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Error: {}".format(rmse))
    print("===== End {} regression ===== \n".format(regression_name))
    return r2
