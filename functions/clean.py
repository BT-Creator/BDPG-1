import math

import numpy as np

from config.clean_params import chained_columns


def clean(df):
    """Main function that cleans data

    :param df: Dataframe
    :return: Cleaned DataFrame
    """
    df.loc[df['LotFrontage'] == -1, 'LotFrontage'] = apply_avg(df, 'LotFrontage', -1)
    df.loc[df['MSZoning'] == "C (all)", 'MSZoning'] = replace_string(df, "MSZoning", "C (all)", "C")
    df.loc[df['BldgType'] == "Twnhs", 'BldgType'] = replace_string(df, "BldgType", "Twnhs", "TwnhsI")
    df.loc[df['BldgType'] == "2fmCon", 'BldgType'] = replace_string(df, "BldgType", "2fmCon", "2FmCon")
    df.loc[df['Exterior2nd'] == "CmentBd", "Exterior2nd"] = replace_string(df, "Exterior2nd", "CmentBd",
                                                                           "CemntBd")
    df.loc[df['Exterior2nd'] == "Brk Cmn", "Exterior2nd"] = replace_string(df, "Exterior2nd", "Brk Cmn",
                                                                           "BrkComm")
    df.loc[df['Exterior2nd'] == "Wd Shng", "Exterior2nd"] = replace_string(df, "Exterior2nd", "Wd Shng",
                                                                           "WdShing")
    df.loc[df['MasVnrType'] == "None", 'MasVnrType'] = replace_string(df, "MasVnrType", "None", None)
    for column in chained_columns:
        df.loc[df[column].isnull()] = fix_relationships_inconsistency(df, column)
    df = apply_most_frequent(df, "MSZoning")
    return df


def apply_avg(df, column, target):
    """Applies the average of columns on selected target. Only works with numerical data!

    :param df: DataFrame
    :param column: Column Name
    :param target: Value to replace
    :return: Modified Column
    """
    avg = int(df[column].mean())
    print("Applying " + str(avg) + " (Average) on " + str(target) + " values in " + column + "...")
    target_column = df.loc[df[column] == target, column]
    target_count = target_column.count()
    target_column = avg
    print("=> Done! Replaced " + str(target_count) + " values.")
    return target_column


def replace_string(df, column, illegal, replacement):
    """ Searches for strings and replaces them

    :param df: DataFrame
    :param column: Column name
    :param illegal: Illegal string
    :param replacement: Replacement value
    :return: Modified Column
    """
    print("Replacing illegal value [ " + illegal + " ] in " + column + "...")
    target_column = df.loc[df[column] == illegal, column]
    target_count = target_column.count()
    target_column = replacement
    print("=> Done! Replaced " + str(target_count) + " values.")
    return target_column


def fix_relationships_inconsistency(df, column):
    """ Fixes faulty relations as defined in `chained_columns` in `data.config`

    :param df: DataFrame
    :param column: Column
    :return: Modified Column
    """
    print("Fixing relationships between " + column + " and it's children")
    target_count = 0
    for dependency in chained_columns.get(column):
        target_count = target_count + df.loc[df[column].isnull(), dependency].count()
        df.loc[df[column].isnull(), dependency] = None
    print("=> Done! Reverted " + str(target_count) + " values to None/NaN.")
    return df


def apply_most_frequent(df, column):
    most_frequent = df[column].mode().values[0]
    df.loc[df[column].isnull(), column] = most_frequent
    return df
