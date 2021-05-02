import matplotlib.pyplot as plt
import seaborn as sn


def generate_correlation_matrix(df):
    """function that generates the correlation matrix

    :param df: Dataframe
    :return: correlation matrix of DataFrame
    """
    corr_matrix = df[df.columns.difference(['Id', 'CentralAir'])].corr()
    plt.subplots(figsize=(30, 30))
    sn.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    return plt


def get_best_correlations(df):
    """function that returns the best correlating elements in the correlation matrix

    :param df: Dataframe
    :return: best correlating elements
    """
    corr_matrix = df.corr()
    corr_matrix = corr_matrix[corr_matrix < 1].unstack().transpose() \
        .sort_values(ascending=False) \
        .drop_duplicates()
    count = corr_matrix[corr_matrix.between(0.5, 1) == True].count()
    return corr_matrix.head(count)
