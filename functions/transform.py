import pandas as pd

from data.config import categorical_values, float_columns, date_columns


def transform(df):
    """Main transform function

    :param df: DataFrame
    :return: Transformed DataFrame
    """
    df['CentralAir'] = df['CentralAir'].astype('bool')
    df[list(categorical_values.keys())] = df[list(categorical_values.keys())].astype('category')
    df[float_columns] = df[float_columns].astype(float)
    df[date_columns.get('year')] = convert_to_date(df, date_columns.get('year'), '%Y')
    df['DateSold'] = pd.to_datetime(df[['YrSold', 'MoSold']]
                                    .rename(columns={'YrSold': 'year', 'MoSold': 'month'})
                                    .assign(DAY=1))
    df = df.drop(['YrSold', 'MoSold'], axis=1)
    return df


def convert_to_date(df, targets, date_format):
    """Transforms multiple columns to Date format

    :param df: DataFrame
    :param targets: Array of column names
    :param date_format: Regex Date format
    :return: Modified columns
    """
    for target in targets:
        df[target] = pd.to_datetime(df[target], format=date_format)
    return df[targets]
