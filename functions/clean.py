def apply_avg(df, column, target):
    print("Applying averages on " + str(target) + " values in " + column + "...")
    target_column = df.loc[df[column] == target, column]
    target_count = target_column.count()
    avg = int(df[column].mean())
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
