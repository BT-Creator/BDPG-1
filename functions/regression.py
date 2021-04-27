from config.regression_params import reg_params


def split_data(train, test):
    X_train = train.drop(reg_params.get('target_column'), axis=1).values
    y_train = train[reg_params.get('target_column')].values
    X_test = test.drop(reg_params.get('target_column'), axis=1).values
    y_test = test[reg_params.get('target_column')].values
    return X_train, X_test, y_train, y_test


