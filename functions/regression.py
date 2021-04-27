from config.regression_params import reg_params


def split_data(train, test):
    y_train = train[reg_params.get('target_column')].values
    X_train = train.drop(reg_params.get('target_column'), axis=1).values
    X_test = test.values
    y_test = None
    return X_train, X_test, y_train, y_test


