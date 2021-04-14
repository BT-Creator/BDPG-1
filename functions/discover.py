import pandas as pd

from data.config import categorical_values, non_strict_columns, chained_columns


def discover_inconsistencies(df):
    print("\n")
    intro_msg = "Discovering irregularities"
    print("#" * (len(intro_msg) + 4))
    print("# " + intro_msg + " #")
    print("#" * (len(intro_msg) + 4))
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
    illegal_values = df[~df[column].isin(categorical_values[column])][column]
    illegal_rows = illegal_values.count()
    if illegal_rows > 0:
        print("- There are", illegal_rows, "rows with illegal string values in column", column)
        return True
    return False


def strict_integer_columns(df, column):
    df[column] = df[column].fillna(-1).astype(int)
    illegal_rows = df[df[column] == -1][column].count()
    if illegal_rows > 0:
        print("- There are", illegal_rows, "rows with NaN values in column", column)
        return True
    return False


def inconsistent_relation(df, column):
    rows = [column] + chained_columns.get(column)
    data = df[rows].where(df[column].isnull())
    for dependency in chained_columns.get(column):
        if pd.Series(data[dependency]).notnull().any():
            print("- For some NA values in " + column + ", the corresponding properties in " + dependency + " is filled in.")
            return True
    return False
