from data.config import chained_columns


def clean(df):
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
    return df


def apply_avg(df, column, target):
    avg = int(df[column].mean())
    print("Applying " + str(avg) + " (Average) on " + str(target) + " values in " + column + "...")
    target_column = df.loc[df[column] == target, column]
    target_count = target_column.count()
    target_column = avg
    print("=> Done! Replaced " + str(target_count) + " values.")
    return target_column


def replace_string(df, column, illegal, replacement):
    print("Replacing illegal value [ " + illegal + " ] in " + column + "...")
    target_column = df.loc[df[column] == illegal, column]
    target_count = target_column.count()
    target_column = replacement
    print("=> Done! Replaced " + str(target_count) + " values.")
    return target_column


def fix_relationships_inconsistency(df, column):
    print("Fixing relationships between " + column + " and it's children")
    target_count = 0
    for dependency in chained_columns.get(column):
        target_count = target_count + df.loc[df[column].isnull(), dependency].count()
        df.loc[df[column].isnull(), dependency] = None
    print("=> Done! Reverted " + str(target_count) + " values to None/NaN.")
    return df
