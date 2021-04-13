import pandas as pd


def convert_to_date(df, targets, date_format):
    for target in targets:
        df[target] = pd.to_datetime(df[target], format=date_format)
    return df[targets]

