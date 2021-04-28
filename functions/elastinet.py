from functions.clean import *
from functions.discover import *
from functions.transform import transform
from sklearn.linear_model import ElasticNet
from sklearn.datasets import make_regression


def calculateElastinet(df):
    reg = ElasticNet()
    data = df
    X, y = [data[:, :1], data[:, -1]]

    print(X)
    print(y)
