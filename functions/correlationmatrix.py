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


def get_best_correlations(df, method):
    """function that returns the best correlating elements in the correlation matrix

    :param df: Dataframe
    :return: best correlating elements
    """
    corr_matrix = df.corr(method)
    cor_target = corr_matrix['SalePrice']
    best_correlations = cor_target[cor_target.between(0.5, 1) == True]
    print("Best correlation to SalePrice \n{}".format(best_correlations))
    return best_correlations.index.tolist()
