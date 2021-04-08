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
