import numpy as np
from skimage.metrics import mean_squared_error
from sklearn.metrics import mean_squared_error

from config.regression_params import reg_params
from functions.discover import *


def split_data(train):
    y = train[reg_params.get('target_column')].values.reshape(-1, 1)
    X = train.drop(reg_params.get('target_column'), axis=1).values
    return X, y


def prep_regression_data(df):
    normalized_columns = df.select_dtypes(include=['number']).columns.tolist()
    normalized_columns.remove('Id')
    if 'SalePrice' in normalized_columns:
        normalized_columns.remove('SalePrice')
    df[normalized_columns] = normalize(df[normalized_columns])
    df['CentralAir'] = df['CentralAir'].replace({True: 1, False: 0})
    for array in chained_columns.values():
        for column in array:
            if df[column].dtype.name is not 'category':
                df[column].fillna(-1, inplace=True)
    df = pd.get_dummies(df)
    return df


def add_missing_possibilities(df, columns):
    for column in columns:
        df[column] = 0
        df[column].astype('uint8')
    return df


def normalize(df):
    norm_df = ((df - df.min()) / (df.max() - df.min()))
    return norm_df


def print_results(regression, X_test, y_test, y_pred, regression_name):
    print("===== {} regression =====".format(regression_name))
    r2 = regression.score(X_test, y_test)
    print("R^2: {}".format(r2))
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Error: {}".format(rmse))
    print("===== End {} regression ===== \n".format(regression_name))
    return rmse


def post_best_predictions(predictions):
    best_prediction = list(predictions.items())[0][0]
    rsme = list(predictions.items())[0][1]
    for key, value in predictions.items():
        if value < rsme:
            best_prediction = key
            rsme = value
    print("The regression method {} has the best prediction with a RMSE of {}".format(
        best_prediction,
        predictions.get(best_prediction)
    ))
