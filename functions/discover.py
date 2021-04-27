import pandas as pd

from config.clean_params import categorical_values, non_strict_columns, chained_columns


def discover_inconsistencies(df):
    """Main method that searches for illegal data

    :param df: A dataframe
    """
    irregularities = 0
    for column in df:
        if column != 'Id' and column in categorical_values:
            if illegal_category_values(df, column):
                irregularities = irregularities + 1
        elif column != 'Id' and column not in non_strict_columns:
            if strict_integer_columns(df, column):
                irregularities = irregularities + 1
        if column != 'Id' and column in chained_columns:
            if inconsistent_relation(df, column):
                irregularities = irregularities + 1
    if irregularities == 0:
        print("Congrats! No data inconsistencies detected.")
    print("\n")


def illegal_category_values(df, column):
    """Returns boolean if illegal categorical values were detected

    It uses the `categorical_values` dictionary in `data.config` in order to detect illegal values.

    :param df: Dataframe
    :param column: Column name of the target column
    :return: boolean
    """
    illegal_values = df[~df[column].isin(categorical_values[column])][column]
    illegal_rows = illegal_values.count()
    if illegal_rows > 0:
        print("- There are", illegal_rows, "rows with illegal string values in column", column)
        return True
    return False


def strict_integer_columns(df, column):
    """Returns boolean if NaN values were detected

    :param df: Dataframe
    :param column: Column name of the target column
    :return: boolean
    """
    df[column] = df[column].fillna(-1).astype(int)
    illegal_rows = df[df[column] == -1][column].count()
    if illegal_rows > 0:
        print("- There are", illegal_rows, "rows with NaN values in column", column)
        return True
    return False


def inconsistent_relation(df, column):
    """Returns boolean if NaN values were detected

    Uses `chained_columns` in `data.config` in order to understand relationships.

    :param df: Dataframe
    :param column: Column name of the target column
    :return: boolean
    """
    rows = [column] + chained_columns.get(column)
    data = df[rows].where(df[column].isnull())
    inconsistencies = 0
    for dependency in chained_columns.get(column):
        if pd.Series(data[dependency]).notnull().any():
            print("- For some NA values in " + column + ", the corresponding properties in " + dependency + " is filled in.")
            inconsistencies = inconsistencies + 1
    return inconsistencies > 0
