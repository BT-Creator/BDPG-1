import matplotlib.pyplot as plt
import seaborn as sn


def generate_correlation_matrix(df):
    """function that generates the correlation matrix

    :param df: Dataframe
    :return: correlation matrix of DataFrame
    """
    corr_matrix = df.corr()
    sn.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    return plt
