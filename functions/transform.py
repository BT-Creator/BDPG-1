import pandas as pd

from data.config import allowed_values, float_columns, date_columns


def transform(df):
    df['CentralAir'] = df['CentralAir'].astype('bool')
    df[list(allowed_values.keys())] = df[list(allowed_values.keys())].astype('category')
    df[float_columns] = df[float_columns].astype(float)
    df[date_columns.get('year')] = convert_to_date(df, date_columns.get('year'), '%Y')
    df['DateSold'] = pd.to_datetime(df[['YrSold', 'MoSold']]
                                    .rename(columns={'YrSold': 'year', 'MoSold': 'month'})
                                    .assign(DAY=1))
    df = df.drop(['YrSold', 'MoSold'], axis=1)
    return df


def convert_to_date(df, targets, date_format):
    for target in targets:
        df[target] = pd.to_datetime(df[target], format=date_format)
    return df[targets]
