from functions.clean import *
from functions.discover import *
from functions.transform import transform
from sklearn.linear_model import ElasticNet
from sklearn.datasets import make_regression


def calculateElastinet(train, test):
    # reg = ElasticNet()
    #
    # data = train.values
    #
    # training_x, training_y = train[:, :-1], train.iloc[:,-1:]
    y = test[["SalePrice"]]

    print(y)



