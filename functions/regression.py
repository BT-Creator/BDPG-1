from sklearn.linear_model import LinearRegression
from config.clean_params import categorical_values, date_columns
from config.regression_params import reg_params


def split_data(train, test):
    train_data = train
    test_data = test.drop(reg_params.get('target_column'), axis=1)
    ref_prices = test[reg_params.get('target_column')]
    return train_data, test_data, ref_prices


def linear_regression(train_data, test_data, ref_prices):
    l_reg = LinearRegression()
    train_data = prep_regression_data(train_data)
    test_data = prep_regression_data(test_data)
    l_reg.fit(test_data[["MSZoning", "LotFrontage"]].values, ref_prices.values)
    print(l_reg.predict(test_data[["MSZoning", "LotFrontage"]].values))


def prep_regression_data(df):
    categorical_columns = list(categorical_values.keys())
    for key in categorical_columns:
        if df[key].isnull().values.any():
            df[key] = df[key].cat.add_categories(-1).fillna(-1)
            df[key] = df[key].cat.remove_categories(None)
        df[key] = df[key].cat.reorder_categories(df[key].unique(), ordered=True)
        df[key] = df[key].cat.codes
    df[df.columns.difference(categorical_columns)].fillna(-1)
    return df
