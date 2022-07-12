import pandas as pd


def get_df():
    yield pd.read_csv('pool_api/data.csv', index_col=0)
