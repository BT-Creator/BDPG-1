def apply_avg(df, column, target):
    avg = int(df[column].mean())
    df[df[column] == target] = avg
