import matplotlib.pyplot as plt
import seaborn as sn

from config.clean_params import chained_columns, categorical_values
from functions.regression.regression_helper import normalize


def generate_correlation_matrix(df, corr_rows, title):
    """function that generates the correlation matrix

    :param df: Dataframe
    :return: correlation matrix of DataFrame
    """
    corr_matrix = df[df.columns.difference(['Id', 'CentralAir'])].corr()
    plt.subplots(figsize=(30, 30))
    heatmap = sn.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    heatmap.set_title(title)
    return plt


def get_best_correlations(df, method):
    """function that returns the best correlating elements in the correlation matrix

    :param method: Method to use for correlation
    :param df: Dataframe
    :return: best correlating elements
    """
    corr_matrix = df.corr(method)
    cor_target = corr_matrix['SalePrice']
    best_correlations = cor_target[cor_target.between(0.5, 1) == True]
    print("Best {} correlation to SalePrice \n{}\n".format(method, best_correlations))
    return best_correlations.index.tolist()


def prep_correlation_data(df):
    normalized_columns = df.select_dtypes(include=['number']).columns.tolist()
    normalized_columns.remove('Id')
    if 'SalePrice' in normalized_columns:
        normalized_columns.remove('SalePrice')
    df[normalized_columns] = normalize(df[normalized_columns])
    df['CentralAir'] = df['CentralAir'].replace({True: 1, False: 0})
    for key in chained_columns.keys():
        if df[key].dtype.name is 'category':
            replace_categorical_na(df, key)
        for column in chained_columns.get(key):
            if df[column].dtype.name is 'category' and df[column].isnull().values.any():
                df[column] = df[column].cat.add_categories(-1).fillna(-1)
                df[column] = df[column].cat.remove_categories(None)
                df[column] = df[column].cat.reorder_categories(df[column].unique(), ordered=True)
                df[column] = df[column].cat.codes
            else:
                df[column].fillna(-1, inplace=True)
    for key in categorical_values.keys():
        if df[key].dtype.name is 'category':
            replace_categorical_na(df, key)
    return df


def replace_categorical_na(df, key):
    if df[key].isnull().values.any():
        df[key] = df[key].cat.add_categories(-1).fillna(-1)
        df[key] = df[key].cat.remove_categories(None)
    df[key] = df[key].cat.reorder_categories(df[key].unique(), ordered=True)
    df[key] = df[key].cat.codes
