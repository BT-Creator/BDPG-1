def apply_avg(df, column, target):
    print("Applying averages on " + str(target) + " values in " + column + "...")
    target_count = df[df[column] == target][column].count()
    avg = int(df[column].mean())
    df[df[column] == target] = avg
    print("=> Done! Replaced " + str(target_count) + " values.")


def replace_string(df, column, illegal, replacement):
    print("Replacing illegal value [ " + illegal + " ] in " + column + "...")
    target_count = df[df[column] == illegal][column].count()
    df[df[column] == illegal] = replacement
    print("=> Done! Replaced " + str(target_count) + " values.")
