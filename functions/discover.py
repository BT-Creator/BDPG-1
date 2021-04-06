def discover_inconsistencies(df, allowed_values):
    intro_msg = "Discovering irregularities"
    print("#" * (len(intro_msg) + 4))
    print("# " + intro_msg + " #")
    print("#" * (len(intro_msg) + 4))
    for column in df:
        if (column != 'Id') and column in allowed_values:
            illegal_values = df[~df[column].isin(allowed_values[column])][column]
            illegal_rows = illegal_values.count()
            if illegal_rows > 0:
                print("- There are", illegal_rows, "rows with illegal string values in column", column)
        elif column != 'Id':
            df[column] = df[column].fillna(-1).astype(int)
            illegal_rows = df[df[column] == -1][column].count()
            if illegal_rows > 0:
                print("- There are", illegal_rows, "rows with NaN values in column", column)
    print("\n")