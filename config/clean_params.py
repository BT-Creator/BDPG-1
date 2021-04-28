"""Contains several variables that determine the cleaning behavior

- `categorical_values` contains all values that are allowed in the dataset. With this, you can quickly check if there is false data in the columns (If the parameters are defined).
- `float_columns` dictates which columns may remain as a float. This was easier, because commonly, only square feet values are allowed to be in float.
- `date_columns` is a dictionary that dictates the date columns. This list has 3 keys: year, month, day. These indicates which type of date the columns has.
- `chained_columns` is a dictionary that defines main columns that influences other columns. If the main columns has a empty value, this will also apply to other columns.
- `non_strict_columns` defined where NaN values are allowed in numerical columns. By default, numerical columns should not have NaN values.
"""
import math

categorical_values = {
    'MSSubClass': [20, 30, 40, 45, 50, 60, 70,
                   75, 80, 85, 90, 120, 150, 160, 180, 190],
    'MSZoning': ['A', 'C', 'FV', 'I', 'RH', 'RL', 'RP', 'RM'],
    'Street': ['Grvl', 'Pave'],
    'Alley': ['Grvl', 'Pave', None],
    'LotShape': ['Reg', 'IR1', 'IR2', 'IR3'],
    'LandContour': ['Lvl', 'Bnk', 'HLS', 'Low'],
    'Utilities': ['AllPub', 'NoSewr', 'NoSeWa', 'ELO'],
    'LotConfig': ['Inside', 'Corner', 'CulDSac', 'FR2', 'FR3'],
    'LandSlope': ['Gtl', 'Mod', 'Sev'],
    'Neighborhood': ['Blmngtn', 'Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr', 'Crawfor',
                     'Edwards', 'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes', 'NoRidge',
                     'NPkVill', 'NridgHt', 'NWAmes', 'OldTown', 'SWISU', 'Sawyer', 'SawyerW', 'Somerst',
                     'StoneBr', 'Timber', 'Veenker'],
    'Condition1': ['Artery', 'Feedr', 'Norm', 'RRNn',
                   'RRAn', 'PosN', 'PosA', 'RRNe', 'RRAe'],
    'Condition2': ['Artery', 'Feedr', 'Norm', 'RRNn',
                   'RRAn', 'PosN', 'PosA', 'RRNe', 'RRAe', None],
    'BldgType': ['1Fam', '2FmCon', 'Duplex', 'TwnhsE', 'TwnhsI'],
    'HouseStyle': ['1Story', '1.5Fin', '1.5Unf',
                   '2Story', '2.5Fin', '2.5Unf', 'SFoyer', 'SLvl'],
    'OverallQual': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'OverallCond': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'RoofStyle': ['Flat', 'Gable', 'Gambrel', 'Hip', 'Mansard', 'Shed'],
    'RoofMatl': ['ClyTile', 'CompShg', 'Membran',
                 'Metal', 'Roll', 'Tar&Grv', 'WdShake', 'WdShngl'],
    'Exterior1st': ['AsbShng', 'AsphShn', 'BrkComm', 'BrkFace', 'CBlock', 'CemntBd', 'HdBoard',
                    'ImStucc', 'MetalSd', 'Other', 'Plywood', 'PreCast', 'Stone', 'Stucco', 'VinylSd', 'Wd Sdng',
                    'WdShing'],
    'Exterior2nd': ['AsbShng', 'AsphShn', 'BrkComm', 'BrkFace', 'CBlock', 'CemntBd', 'HdBoard',
                    'ImStucc', 'MetalSd', 'Other', 'Plywood', 'PreCast', 'Stone', 'Stucco', 'VinylSd', 'Wd Sdng',
                    'WdShing', None],
    'MasVnrType': ['BrkCmn', 'BrkFace', 'CBlock', None, 'Stone'],
    'ExterQual': ['Ex', 'Gd', 'TA', 'Fa', 'Po'],
    'ExterCond': ['Ex', 'Gd', 'TA', 'Fa', 'Po'],
    'Foundation': ['BrkTil', 'CBlock', 'PConc', 'Slab', 'Stone', 'Wood'],
    'BsmtQual': ['Ex', 'Gd', 'TA', 'Fa', 'Po', None],
    'BsmtCond': ['Ex', 'Gd', 'TA', 'Fa', 'Po', None],
    'BsmtExposure': ['Gd', 'Av', 'Mn', 'No', None],
    'BsmtFinType1': ['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', None],
    'BsmtFinType2': ['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', None],
    'Heating': ['Floor', 'GasA', 'GasW', 'Grav', 'OthW', 'Wall'],
    'HeatingQC': ['Ex', 'Gd', 'TA', 'Fa', 'Po'],
    'CentralAir': ['N', 'Y'],
    'Electrical': ['SBrkr', 'FuseA', 'FuseF', 'FuseP', 'Mix'],
    'KitchenQual': ['Ex', 'Gd', 'TA', 'Fa', 'Po'],
    'Functional': ['Typ', 'Min1', 'Min2', 'Mod', 'Maj1', 'Maj2', 'Sev', 'Sal'],
    'FireplaceQu': ['Ex', 'Gd', 'TA', 'Fa', 'Po', None],
    'GarageType': ['2Types', 'Attchd', 'Basment',
                   'BuiltIn', 'CarPort', 'Detchd', None],
    'GarageFinish': ['Fin', 'RFn', 'Unf', None],
    'GarageQual': ['Ex', 'Gd', 'TA', 'Fa', 'Po', None],
    'GarageCond': ['Ex', 'Gd', 'TA', 'Fa', 'Po', None],
    'PavedDrive': ['Y', 'P', 'N'],
    'PoolQC': ['Ex', 'Gd', 'TA', 'Fa', None],
    'Fence': ['GdPrv', 'MnPrv', 'GdWo', 'MnWw', None],
    'MiscFeature': ['Elev', 'Gar2', 'Othr', 'Shed', 'TenC', None],
    'SaleType': ['WD', 'CWD', 'VWD', 'New', 'COD',
                 'Con', 'ConLw', 'ConLI', 'ConLD', 'Oth'],
    'SaleCondition': ['Normal', 'Abnorml',
                      'AdjLand', 'Alloca', 'Family', 'Partial']
}

float_columns = ['LotArea', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF',
                 '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch',
                 '3SsnPorch', 'ScreenPorch', 'PoolArea']


date_columns = {
    'year': ['YearBuilt', 'YearRemodAdd', 'GarageYrBlt'],
    'month': [],
    'day': [],
}

chained_columns = {
    'BsmtQual': ['BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath'],
    'GarageType': ['GarageYrBlt', 'GarageFinish', 'GarageArea', 'GarageQual', 'GarageCond'],
    'MasVnrType': ['MasVnrArea']
}

non_strict_columns = ['BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath', 'GarageCars', 'GarageArea', 'GarageYrBlt', 'MasVnrArea']